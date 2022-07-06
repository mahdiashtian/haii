from dataclasses import field
from rest_framework import serializers
from .models import Startup


class StartupSerializers(serializers.ModelSerializer):
    class Meta:
        model = Startup
        fields = '__all__'