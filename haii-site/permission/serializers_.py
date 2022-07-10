from rest_framework import serializers
from .models import Permission


class PermissionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'
