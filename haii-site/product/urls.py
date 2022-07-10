from django.urls import path, include
from .views import ProductViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')

app_name = 'product'

urlpatterns = [
    path('v1/', include(router.urls))
]
