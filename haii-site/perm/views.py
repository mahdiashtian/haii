from django.contrib.auth.models import Permission
from rest_framework import viewsets, mixins

from .models import Perm
from .serializers_ import PermissionSerializer, PermSerializer


class PermViewSet(viewsets.ModelViewSet):
    queryset = Perm.objects.all()
    serializer_class = PermSerializer
    model = Perm


class PermissionViewSet(mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    model = Permission
