from product.serializers_ import ProductSerializers
from rest_framework import serializers

from .models import Team


class TeamSerializers(serializers.ModelSerializer):
    product = ProductSerializers(many=True, read_only=True)

    class Meta:
        model = Team
        fields = '__all__'
