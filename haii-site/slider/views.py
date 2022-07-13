from rest_framework import viewsets
from utils.mixins import PermissionMixin
from .models import Slider
from .serializers_ import SliderSerializers


class SliderViewSet(PermissionMixin,viewsets.ModelViewSet):
    queryset = Slider.objects.filter(active=True)
    serializer_class = SliderSerializers
    model = Slider

