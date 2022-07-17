from django.contrib.auth import get_permission_codename
from rest_framework.permissions import BasePermission

from .models import Perm


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
        pr = Perm.objects.filter(user=request.user)
        if pr and pr.first().has_perm(perm=perm, model=model, item=id_):
            return True
        return False


class IsAdder(BasePermission):
    def has_permission(self, request, view):
        model = view.model
        opts = model._meta
        perm = "%s.%s" % (opts.app_label, get_permission_codename('add', opts))
        pr = Perm.objects.filter(user=request.user)
        if pr and pr.first().has_perm(perm=perm, model=model):
            return True
        return False


class IsRemoval(BasePermission):
    def has_object_permission(self, request, view, obj):
        model = view.model
        opts = model._meta
        perm = "%s.%s" % (opts.app_label, get_permission_codename('delete', opts))
        id_ = obj.id
        pr = Perm.objects.filter(user=request.user)
        if pr and pr.first().has_perm(perm=perm, model=model, item=id_):
            return True
        return False


class IsViewer(BasePermission):
    def has_permission(self, request, view):
        model = view.model
        opts = model._meta
        perm = "%s.%s" % (opts.app_label, get_permission_codename('view', opts))
        pr = Perm.objects.filter(user=request.user)
        if pr and pr.first().has_perm(perm=perm, model=model):
            return True
        return False


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
