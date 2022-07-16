from django.urls import path, include
from rest_framework import routers

from .views import PermissionViewSet, PermViewSet

router = routers.DefaultRouter()
router.register(r'perm', PermViewSet, basename='perm')
router.register(r'permission', PermissionViewSet, basename='permission')

app_name = 'perm'

urlpatterns = [
    path('v1/', include(router.urls))
]
