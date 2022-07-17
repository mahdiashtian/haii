from log_admin.mixins import LogAdminMixin
from perm.mixins import PermissionMixin
from rest_framework import viewsets

from .models import Startup
from .serializers_ import StartupSerializers


class StartupViewSet(LogAdminMixin, PermissionMixin, viewsets.ModelViewSet):
    serializer_class = StartupSerializers
    queryset = Startup.objects.all()
    model = Startup
