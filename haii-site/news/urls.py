from django.urls import path, include
from .views import NewsViewSet, TagViewSet, CategoryViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'news', NewsViewSet, basename='news')
router.register(r'tag', TagViewSet, basename='tag')
router.register(r'category', CategoryViewSet, basename='category')

app_name = 'news'

urlpatterns = [
    path('v1/', include(router.urls))
]
