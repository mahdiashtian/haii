from rest_framework import serializers
from .models import User
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.password_validation import validate_password


class PermissionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class GroupSerializers(serializers.ModelSerializer):
    permissions_ = PermissionSerializers(source='permissions',many=True,read_only=True)
    class Meta:
        model = Group

        fields = [
            'id',
            'name',
            'permissions_',
            'permissions'
        ]

        extra_kwargs = {
            'permissions':{'write_only':True},
        }


class UserSerializers(serializers.ModelSerializer):
    user_permissions_ = PermissionSerializers(source='user_permissions',many=True,read_only=True)

    groups_ = GroupSerializers(source='groups',many=True,read_only=True)

    class Meta:
        model = User

        fields = [
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'last_login',
            'date_joined',
            'is_superuser',
            'is_staff',
            'is_active',
            'user_permissions',
            'groups',
            'user_permissions_',
            'groups_',
        ]

        extra_kwargs = {
            'groups':{'write_only':True},
            'user_permissions':{'write_only':True},
        }


class ChangePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value