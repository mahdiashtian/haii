from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from utils.mixins import LogAdminMixin
from .models import News, Tag, Category
from .serializers_ import NewsSerializer, CategorySerializer, TagSerializer


class NewsViewSet(LogAdminMixin, viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    model = News
    ordering_fields = ['date_of_registration']
    search_fields = ['category__name', 'tag__name', 'name', 'news']
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
