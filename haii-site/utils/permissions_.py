from rest_framework.permissions import BasePermission
from django.contrib.auth import get_permission_codename
from django.contrib.contenttypes.models import ContentType


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_superuser)


class IsEditor(BasePermission):
    def has_permission(self, request, view):
        opts = view.model._meta
        return bool(
        request.user.has_perm(
                 "%s.%s" % (opts.app_label, get_permission_codename('change', opts))
             )
        )


    def has_object_permission(self, request, view, obj):
        user = request.user
        ct = ContentType.objects.get_for_model(view.model)
        if obj.group.filter(user=request.user).exists() or user.groups.all().filter(owner_content_type_id=ct.id,is_admin=True).exists():
            return True
        else:
            return False


class IsAdder(BasePermission):
    def has_permission(self, request, view):
        opts = view.model._meta
        return bool(
        request.user.has_perm(
                 "%s.%s" % (opts.app_label, get_permission_codename('add', opts))
             )

        )


class IsRemoval(BasePermission):
    def has_permission(self, request, view):
        opts = view.model._meta
        return bool(
        request.user.has_perm(
                 "%s.%s" % (opts.app_label, get_permission_codename('delete', opts))
             )
        )


    def has_object_permission(self, request, view, obj):
        user = request.user
        ct = ContentType.objects.get_for_model(view.model)
        if obj.group.filter(user=request.user).exists() or user.groups.all().filter(owner_content_type_id=ct.id,
                                                                                    is_admin=True).exists():
            return True
        else:
            return False


class IsViewer(BasePermission):
    def has_permission(self, request, view):
        opts = view.model._meta
        return bool(
        request.user.has_perm(
                 "%s.%s" % (opts.app_label, get_permission_codename('view', opts))
             )
        )


    def has_object_permission(self, request, view, obj):
        user = request.user
        ct = ContentType.objects.get_for_model(view.model)
        if obj.group.filter(user=request.user).exists() or user.groups.all().filter(owner_content_type_id=ct.id,
                                                                                    is_admin=True).exists():
            return True
        else:
            return False


class ReturnPerm():
    def __init__(self):
        self.dict_perm = {
            'list':IsViewer,
            'retrieve':IsViewer,
            'create':IsAdder,
            'update':IsEditor,
            'partial_update':IsEditor,
            'destroy':IsRemoval,
        }

    def get_prm(self,action):
        return self.dict_perm[action]