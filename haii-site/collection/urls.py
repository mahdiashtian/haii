from django.urls import path, include
from rest_framework import routers

from .views import StartupViewSet
from .views import TeamViewSet

router = routers.DefaultRouter()
router.register(r'startup', StartupViewSet, basename='startup')
router.register(r'team', TeamViewSet, basename='team')

app_name = 'collection'

urlpatterns = [
    path('v1/', include(router.urls))
]
