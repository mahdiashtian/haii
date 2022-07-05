from rest_framework import viewsets
from .models import Team
from .serializers_ import TeamSerializers
from utils.mixins import PermissiomMixin 


class TeamViewSet(PermissiomMixin,viewsets.ModelViewSet):
    serializer_class = TeamSerializers
    model = Team
    queryset = Team.objects.all()