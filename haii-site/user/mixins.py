from tokenize import group
from distro import codename
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import Group , Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_permission_codename
from django.db.models import Q
from django.db import transaction
from user.models import User

from .permission_ import (
    IsSuperUser,
    IsEditor,
    IsAdder,
    IsRemoval,
    IsListViewer,
    IsRetrieveView
)


class PerformCreateMixin:
    def perform_create(self, serializer):
        user = self.request.user
        model = self.model
        opts = model._meta
        instance = serializer.save()
        content_type = instance.owner_content_type
        object_id = instance.owner_object_id
        excludes = [
            f"add_{model._meta.model_name}"
        ]
        permission = Permission.objects.filter(Q(content_type=content_type) & ~Q(codename__in=excludes))
        gp = Group.objects.create(content_type=content_type,object_id=instance.id,name='مجوز '+instance.name)
        gp.permissions.set(permission)
        perm = get_permission_codename('add', opts)
        users = User.objects.filter(
            Q(groups__content_type=content_type) & Q(groups__object_id=object_id)
            ).distinct().filter(groups__permissions__codename=perm)
        with transaction.atomic():
            for user in users:
                user.groups.add(gp)


class PermissionMixin:
    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        # if self.action == 'list':
        #     permission_classes += [IsSuperUser | IsListViewer]
            
        # if self.action == 'retrieve':
        #     permission_classes += [IsSuperUser | IsRetrieveView]

        if self.action == 'create':
            permission_classes += [IsSuperUser | IsAdder]

        elif self.action in ['update', 'partial_update']:
            permission_classes += [IsSuperUser | IsEditor]

        elif self.action == 'destroy':
            permission_classes += [IsSuperUser | IsRemoval]

        return [permission() for permission in permission_classes]
