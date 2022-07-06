from dataclasses import fields
from rest_framework import serializers
from .models import Team


class TeamSerializers(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'