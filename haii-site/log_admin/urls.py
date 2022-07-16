from django.urls import path, include
from .views import LogViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'log', LogViewSet, basename='log')

app_name = 'log'

urlpatterns = [
    path('v1/', include(router.urls))
]
