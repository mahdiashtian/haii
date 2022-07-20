from django.urls import path, include
from rest_framework import routers

from .views import NewsViewSet

router = routers.DefaultRouter()
router.register(r'news', NewsViewSet, basename='news')

app_name = 'news'

urlpatterns = [
    path('v1/', include(router.urls))
]
