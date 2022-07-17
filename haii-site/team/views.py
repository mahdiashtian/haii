from log_admin.mixins import LogAdminMixin
from perm.mixins import PermissionMixin
from rest_framework import viewsets

from .models import Team
from .serializers_ import TeamSerializers


class TeamViewSet(LogAdminMixin, PermissionMixin, viewsets.ModelViewSet):
    serializer_class = TeamSerializers
    model = Team
    queryset = Team.objects.all()
