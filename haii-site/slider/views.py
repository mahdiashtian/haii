from log_admin.mixins import LogAdminMixin
from perm.mixins import PermissionMixin
from rest_framework import viewsets

from .models import Slider
from .serializers_ import SliderSerializers


class SliderViewSet(LogAdminMixin, PermissionMixin, viewsets.ModelViewSet):
    queryset = Slider.objects.filter(active=True)
    serializer_class = SliderSerializers
    model = Slider
