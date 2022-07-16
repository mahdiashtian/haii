from rest_framework import viewsets
from log_admin.mixins import LogAdminMixin

from .models import Slider
from .serializers_ import SliderSerializers


class SliderViewSet(LogAdminMixin, viewsets.ModelViewSet):
    queryset = Slider.objects.filter(active=True)
    serializer_class = SliderSerializers
    model = Slider
