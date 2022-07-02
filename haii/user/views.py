from django.shortcuts import render
from rest_framework import viewsets
from .serializers_ import UserSerializers , GroupSerializers , PermissionSerializers
from .models import User
from django.contrib.auth.models import Group, Permission
from utils.permissions_ import IsSuperUser

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.all()
    permission_classes = [IsSuperUser]
    

class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializers
    queryset = Group.objects.all()
    permission_classes = [IsSuperUser]


class PermissionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PermissionSerializers
    queryset = Permission.objects.all()
    permission_classes = [IsSuperUser]