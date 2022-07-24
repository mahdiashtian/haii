from log_admin.mixins import LogAdminMixin
from rest_framework import viewsets

from .models import Category, Tag
from .serializers_ import CategorySerializer, TagSerializer


class TagViewSet(LogAdminMixin, viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CategoryViewSet(LogAdminMixin, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    model = Category
