from log_admin.mixins import LogAdminMixin
from rest_framework import viewsets

from .models import Team
from .serializers_ import TeamSerializers


class TeamViewSet(LogAdminMixin, viewsets.ModelViewSet):
    serializer_class = TeamSerializers
    model = Team
    queryset = Team.objects.all()
