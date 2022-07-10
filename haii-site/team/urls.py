from django.urls import path, include
from .views import TeamViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'team', TeamViewSet, basename='team')

app_name = 'team'

urlpatterns = [
    path('v1/', include(router.urls))
]
