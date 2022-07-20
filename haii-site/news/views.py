from django_filters.rest_framework import DjangoFilterBackend
from log_admin.mixins import LogAdminMixin
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import News
from .serializers_ import NewsSerializer


class NewsViewSet(LogAdminMixin, viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    model = News
    ordering_fields = ['date_of_registration']
    search_fields = ['category__name', 'tag__name', 'name', 'news']
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
