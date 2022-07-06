from django.urls import path , include
from .views import StartupViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'startup', StartupViewSet,basename='startup')


app_name = 'startup'


urlpatterns = [
    path('v1/',include(router.urls))
]