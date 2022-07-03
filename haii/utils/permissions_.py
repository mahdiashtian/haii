from rest_framework.permissions import BasePermission
from django.contrib.auth import get_permission_codename


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsEditor(BasePermission):
    def has_permission(self, request, view):
        opts = view.model._meta
        return bool(
        request.user.has_perm(
                 "%s.%s" % (opts.app_label, get_permission_codename('change', opts))
             )
        )


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


class IsViewer(BasePermission):
    def has_permission(self, request, view):
        opts = view.model._meta
        return bool(
        request.user.has_perm(
                 "%s.%s" % (opts.app_label, get_permission_codename('view', opts))
             )
        )


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