from rest_framework import serializers
from .models import Product
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError


class ProductSerializers(serializers.ModelSerializer):
    def validate(self, attrs):
        owner_content_type = attrs['owner_content_type']
        owner_object_id = attrs['owner_object_id']

        qs = ContentType.objects.filter(id=owner_content_type.id).first().model_class().objects.filter(id=owner_object_id).exists()
        if qs:
            return attrs
        raise ValidationError({'owner_object_id': 'هیچ آیتمی با این آیدی وجود ندارد.'})


    class Meta:
        model = Product
        fields = '__all__'