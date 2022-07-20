from django.urls import path, include
from rest_framework import routers

from .views import TagViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'tag', TagViewSet, basename='tag')
router.register(r'category', CategoryViewSet, basename='category')

app_name = 'bookmark'

urlpatterns = [
    path('v1/', include(router.urls))
]
