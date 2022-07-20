from log_admin.mixins import LogAdminMixin
from rest_framework import viewsets

from .models import Slider
from .serializers_ import SliderSerializers


class SliderViewSet(LogAdminMixin, viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializers
    model = Slider
