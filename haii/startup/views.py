from django.shortcuts import render
from rest_framework import viewsets
from .models import Startup
from .serializers_ import StartupSerializers
from utils.mixins import PermissiomMixin
    
    
class StartupViewSet(PermissiomMixin,viewsets.ModelViewSet):
    serializer_class = StartupSerializers
    queryset = Startup.objects.all()
    model = Startup