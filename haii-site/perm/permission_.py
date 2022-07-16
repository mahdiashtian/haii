from django.contrib.auth import get_permission_codename
from django.contrib.contenttypes.models import ContentType
from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)

    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_superuser)


class IsEditor(BasePermission):
    def has_object_permission(self, request, view, obj):
        model = view.model
        opts = model._meta
        perm = "%s.%s" % (opts.app_label, get_permission_codename('change', opts))
        id_ = obj.id
        return bool(
            request.user.has_perm_custom(
                perm=perm, model=model, id=id_
            )
        )


class IsAdder(BasePermission):
    def has_permission(self, request, view):
        model = view.model
        opts = model._meta
        perm = "%s.%s" % (opts.app_label, get_permission_codename('add', opts))
        return bool(
            request.user.has_perm_custom(
                perm=perm, model=model
            )
        )


class IsRemoval(BasePermission):
    def has_object_permission(self, request, view, obj):
        model = view.model
        opts = model._meta
        perm = "%s.%s" % (opts.app_label, get_permission_codename('delete', opts))
        id_ = obj.id
        return bool(
            request.user.has_perm_custom(
                perm=perm, model=model, id=id_
            )
        )


class IsViewer(BasePermission):
    def has_permission(self, request, view):
        model = view.model
        opts = model._meta
        perm = "%s.%s" % (opts.app_label, get_permission_codename('view', opts))
        return bool(
            request.user.has_perm_custom(
                perm=perm, model=model
            )
        )


class ReturnPerm():
    def __init__(self):
        self.dict_perm = {
            'list': IsViewer,
            'retrieve': IsViewer,
            'create': IsAdder,
            'update': IsEditor,
            'partial_update': IsEditor,
            'destroy': IsRemoval,
        }

    def get_prm(self, action):
        return self.dict_perm[action]
