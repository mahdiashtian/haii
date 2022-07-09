from rest_framework import serializers
from .models import User
from django.contrib.auth.models import Permission , Group
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.models import ContentType


class PermissionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class GroupSerializers(serializers.ModelSerializer):
    def validate(self, attrs):
        user = self.context['request'].user
        owner_content_type = attrs.get('owner_content_type',None)
        owner_object_id = attrs.get('owner_object_id',None)
        is_admin = attrs.get('is_admin',None)

        qs = ContentType.objects.filter(id=owner_content_type.id).first().model_class().objects.filter(id=owner_object_id)

        if is_admin or qs.exists():
            attrs['creator'] = self.context['request'].user
            return attrs
        raise ValidationError({'owner_object_id': 'هیچ آیتمی با این آیدی وجود ندارد.'})


    def validate_permissions(self,value):
        func = lambda x: f'{x.content_type.app_label}.{x.codename}'
        to_set = set(map(func,value))
        user = self.context['request'].user
        if user.has_perms(to_set):
            return value
        raise ValidationError({'permissions': 'شما حق انجام این عملیات را ندارید.'})


    @staticmethod
    def get_owner_object(obj):
        query = obj.owner_content_type.model_class().objects.filter(id=obj.owner_object_id).first()
        if query:
            return query.name
        return None


    permissions_ = PermissionSerializers(source='permissions',many=True,read_only=True)

    owner = serializers.StringRelatedField(source='owner_content_type',read_only=True)

    owner_object = serializers.SerializerMethodField()

    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Group

        fields = [
            'id',
            'name',
            'permissions_',
            'permissions',
            'owner_content_type',
            'owner_object_id',
            'owner',
            'owner_object',
            'is_admin',
            'creator',
        ]

        extra_kwargs = {
            'permissions': {'write_only':True},
            'owner_content_type': {'write_only':True},
            'owner_object_id': {'write_only':True},
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