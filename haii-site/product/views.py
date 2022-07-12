from unittest import result
from rest_framework import viewsets
from .models import Product
from .serializers_ import ProductSerializers
from user.models import Group, User
from utils.mixins import PermissionMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter , OrderingFilter


class ProductViewSet(PermissionMixin,viewsets.ModelViewSet):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    model = Product
    ordering_fields = ['date']
    search_fields = ['category__name','tag__name','name','description']
    filter_fields = ('owner_content_type',)
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
