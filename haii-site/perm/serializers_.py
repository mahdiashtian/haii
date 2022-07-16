from django.contrib.auth.models import Permission
from rest_framework import serializers

from .models import Perm


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class PermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perm
        fields = '__all__'
