from product.serializers_ import ProductSerializers
from rest_framework import serializers

from .models import Team, Startup


class StartupSerializers(serializers.ModelSerializer):
    product = ProductSerializers(many=True, read_only=True)

    class Meta:
        model = Startup
        fields = '__all__'


class TeamSerializers(serializers.ModelSerializer):
    product = ProductSerializers(many=True, read_only=True)

    class Meta:
        model = Team
        fields = '__all__'
