from django.shortcuts import render
from rest_framework import viewsets
from .models import Permission
from .serializers_ import PermissionSerializers


class PermissionViewSet(viewsets.ModelViewSet):
    serializer_class = PermissionSerializers
    queryset = Permission.objects.all()
