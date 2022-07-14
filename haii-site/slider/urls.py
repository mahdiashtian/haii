from django.urls import path, include
from rest_framework import routers

from .views import SliderViewSet

router = routers.DefaultRouter()
router.register(r'slider', SliderViewSet, basename='slider')

app_name = 'slider'

urlpatterns = [
    path('v1/', include(router.urls))
]
