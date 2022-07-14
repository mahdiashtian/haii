from django.urls import path, include
from rest_framework import routers

from .views import TeamViewSet

router = routers.DefaultRouter()
router.register(r'team', TeamViewSet, basename='team')

app_name = 'team'

urlpatterns = [
    path('v1/', include(router.urls))
]
