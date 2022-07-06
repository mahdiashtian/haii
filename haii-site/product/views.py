from unittest import result
from rest_framework import viewsets
from utils.mixins import PermissiomMixin
from .models import Product
from .serializers_ import ProductSerializers
from user.models import Group,User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


class ProductViewSet(PermissiomMixin,viewsets.ModelViewSet):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    model = Product


    def perform_create(self, serializer):
        super().perform_create(serializer)
        user = self.request.user
        instance = serializer.data
        conetent_type = ContentType.objects.get_for_model(self.model)
        permissions = Permission.objects.filter(content_type__id=conetent_type.id)
        name = instance['name']
        group = Group.objects.create(name=f'مدیریت محصول {name}',owner_content_type=conetent_type,owner_object_id=instance['id'])
        group.permissions.set(permissions)
        result = User.objects.get(id=user.id)
        result.groups.add(group)