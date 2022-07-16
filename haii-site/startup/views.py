from rest_framework import viewsets

from log_admin.mixins import LogAdminMixin
from .models import Startup
from .serializers_ import StartupSerializers


class StartupViewSet(LogAdminMixin, viewsets.ModelViewSet):
    serializer_class = StartupSerializers
    queryset = Startup.objects.all()
    model = Startup
