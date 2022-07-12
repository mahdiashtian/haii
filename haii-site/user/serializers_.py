from rest_framework import serializers
from .models import User
from django.contrib.auth.models import Permission
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.models import ContentType


class PermissionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    perm_ = serializers.ReadOnlyField(source="to_dict")

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
            'perm',
            'perm_',
        ]

        extra_kwargs = {
            'perm': {'write_only': True},
        }


class ChangePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)


    def validate_new_password(self, value):
        validate_password(value)
        return value