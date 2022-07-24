from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.db.models import Q

from .models import Product


class ProductSerializers(serializers.ModelSerializer):
    def validate(self, attrs):
        user = self.context['request'].user
        owner_content_type = attrs['owner_content_type']
        owner_object_id = attrs['owner_object_id']
        model_by_content_type = ContentType.objects.filter(id=owner_content_type.id).first().model_class()
        result = model_by_content_type.objects.filter(
            id=owner_object_id
            ).exists()
        user_ = user.groups.filter(
            (
                Q(content_type=owner_content_type) & Q(object_id=owner_object_id)
            )
            |
            (
                Q(content_type=owner_content_type) & Q(overall=True)
            )
        ).distinct().exists()
        if result and user_:
            return attrs
        raise ValidationError({
            'object_id' : 'هیچ آیتمی با این آیدی وجود ندارد.' if not result else None ,
            'permission':'شما حق انجام این کار را ندارید'  if not user_ else None ,
            })


    class Meta:
        model = Product
        fields = '__all__'
