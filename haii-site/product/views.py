from django_filters.rest_framework import DjangoFilterBackend
from log_admin.mixins import LogAdminMixin
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from user.mixins import PerformCreateMixin

from .models import Product
from .serializers_ import ProductSerializers


class ProductViewSet(PerformCreateMixin,LogAdminMixin, viewsets.ModelViewSet):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    model = Product
    ordering_fields = ['date']
    search_fields = ['category__name', 'tag__name', 'name', 'description']
    filter_fields = ('owner_content_type',)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
