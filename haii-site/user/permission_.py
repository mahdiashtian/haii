from django.contrib.auth import get_permission_codename
from rest_framework.permissions import BasePermission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group
from django.db.models import Q


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)

    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_superuser)


class IsEditor(BasePermission):
    def has_object_permission(self, request, view, obj):
        model = view.model
        opts = model._meta
        id_ = obj.id
        user = request.user
        perm = get_permission_codename('change',opts)
        content_type = ContentType.objects.get_for_model(model)
        lookup = (
            (Q(content_type=content_type) & Q(object_id=id_) & Q(user=user) & Q(permissions__codename=perm)) | (Q(content_type=content_type) & Q(overall=True) & Q(user=user) & Q(permissions__codename=perm))
        )
        result = Group.objects.filter(lookup).exists()
        if result:
            return True
        return False


class IsAdder(BasePermission):
    def has_permission(self, request, view):
        model = view.model
        opts = model._meta
        perm = "%s.%s" % (opts.app_label, get_permission_codename('add', opts))
        user = request.user
        if user.has_perm(perm):
            return True
        return False


class IsRemoval(BasePermission):
    def has_object_permission(self, request, view, obj):
        model = view.model
        id_ = obj.id
        user = request.user
        content_type = ContentType.objects.get_for_model(model)
        opts = model._meta
        perm = get_permission_codename('change',opts)
        lookup = (
            (Q(content_type=content_type) & Q(object_id=id_) & Q(user=user) & Q(permissions__codename=perm)) | (Q(content_type=content_type) & Q(overall=True) & Q(user=user) & Q(permissions__codename=perm))
        )
        result = Group.objects.filter(lookup).exists()
        if result:
            return True
        return False


class IsRetrieveView(BasePermission):
    def has_object_permission(self, request, view, obj):
        model = view.model
        id_ = obj.id
        user = request.user
        content_type = ContentType.objects.get_for_model(model)
        opts = model._meta
        perm = get_permission_codename('change',opts)
        lookup = (
            (Q(content_type=content_type) & Q(object_id=id_) & Q(user=user) & Q(permissions__codename=perm)) | (Q(content_type=content_type) & Q(overall=True) & Q(user=user) & Q(permissions__codename=perm))
        )
        result = Group.objects.filter(lookup).exists()
        if result:
            return True
        return False


class IsListViewer(BasePermission):
    def has_permission(self, request, view):
        model = view.model
        opts = model._meta
        perm = "%s.%s" % (opts.app_label, get_permission_codename('view', opts))
        user = request.user
        if user.has_perm(perm):
            return True
        return False


class ReturnPerm():
    def __init__(self):
        self.dict_perm = {
            'list': IsListViewer,
            'retrieve': IsRetrieveView,
            'create': IsAdder,
            'update': IsEditor,
            'partial_update': IsEditor,
            'destroy': IsRemoval,
        }

    def get_prm(self, action):
        return self.dict_perm[action]
