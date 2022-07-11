from django.urls import path, include
from .views import UserViewSet, PermissionViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'permission', PermissionViewSet, basename='permission')

app_name = 'users'

urlpatterns = [
    path('v1/admin/', include(router.urls))
]
