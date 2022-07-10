from django.urls import path, include
from .views import PermissionViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'permission', PermissionViewSet, basename='permission')

app_name = 'permission'

urlpatterns = [
    path('v1/', include(router.urls))
]
