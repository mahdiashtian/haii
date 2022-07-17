from django.contrib.auth.models import Permission
from log_admin.mixins import LogAdminMixin
from rest_framework import viewsets, mixins

from .mixins import PermissionMixin
from .models import Perm
from .serializers_ import PermissionSerializer, PermSerializer


class PermViewSet(LogAdminMixin, PermissionMixin, viewsets.ModelViewSet):
    queryset = Perm.objects.all()
    serializer_class = PermSerializer
    model = Perm


class PermissionViewSet(mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    model = Permission
