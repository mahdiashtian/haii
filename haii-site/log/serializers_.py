from dataclasses import field
from rest_framework import serializers
from .models import Log


class LogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'