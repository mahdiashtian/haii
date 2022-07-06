from django.db import models
from utils.utils import upload_image_path
from django.contrib.contenttypes.fields import GenericForeignKey , GenericRelation
from django.contrib.contenttypes.models import ContentType


class Product(models.Model):
    name = models.CharField(verbose_name='نام',max_length=50)

    description = models.TextField(verbose_name='توضیحات')

    image = models.ImageField(verbose_name='لوگو',upload_to=upload_image_path,null=True,blank=True,)

    date = models.DateTimeField(auto_now_add=True,verbose_name='سال ساخت')

    limit = models.Q(app_label = 'startup', model = 'startup') | models.Q(app_label = 'team', model = 'team')

    owner_content_type = models.ForeignKey(ContentType,
        on_delete=models.CASCADE, 
        related_name="owner_product_content_type",
        limit_choices_to = limit,)

    owner_object_id = models.PositiveIntegerField()

    owner_instance = GenericForeignKey('owner_content_type', 'owner_object_id')

    group = GenericRelation('user.CustomGroup', content_type_field='owner_content_type', object_id_field='owner_object_id')


    def __str__(self):
        return self.name


    class Meta:
        app_label = "product"
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
        base_manager_name = "objects"
        ordering = ['date']