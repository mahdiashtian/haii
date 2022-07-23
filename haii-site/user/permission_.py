from django.contrib.auth import get_permission_codename
from rest_framework.permissions import BasePermission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group


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
        user = request.user
        content_type = ContentType.objects.get_for_model(model)
        result = Group.objects.filter(content_type=content_type,object_id=id_,user=user).exists()
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
        result = Group.objects.filter(content_type=content_type,object_id=id_,user=user).exists()
        if result:
            return True
        return False


class IsRetrieveView(BasePermission):
    def has_object_permission(self, request, view, obj):
        model = view.model
        id_ = obj.id
        user = request.user
        content_type = ContentType.objects.get_for_model(model)
        result = Group.objects.filter(content_type=content_type,object_id=id_,user=user).exists()
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
            'list': IsViewer,
            'retrieve': IsViewer,
            'create': IsAdder,
            'update': IsEditor,
            'partial_update': IsEditor,
            'destroy': IsRemoval,
        }

    def get_prm(self, action):
        return self.dict_perm[action]
