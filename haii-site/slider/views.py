from rest_framework import viewsets

from .models import Slider
from .serializers_ import SliderSerializers


class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.filter(active=True)
    serializer_class = SliderSerializers
    model = Slider
