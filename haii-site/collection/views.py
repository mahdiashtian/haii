from log_admin.mixins import LogAdminMixin
from rest_framework import viewsets

from .models import Startup, Team
from .serializers_ import StartupSerializers, TeamSerializers
from user.mixins import  PermissionMixin


class StartupViewSet(PermissionMixin,LogAdminMixin, viewsets.ModelViewSet):
    serializer_class = StartupSerializers
    queryset = Startup.objects.all()
    model = Startup


class TeamViewSet(PermissionMixin,LogAdminMixin, viewsets.ModelViewSet):
    serializer_class = TeamSerializers
    model = Team
    queryset = Team.objects.all()
