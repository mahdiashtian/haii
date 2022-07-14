from rest_framework import viewsets

from utils.mixins import LogAdminMixin
from .models import Team
from .serializers_ import TeamSerializers


class TeamViewSet(LogAdminMixin, viewsets.ModelViewSet):
    serializer_class = TeamSerializers
    model = Team
    queryset = Team.objects.all()
