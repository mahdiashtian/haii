from django.db import models
from utils.utils import upload_image_path
from django.contrib.contenttypes.fields import GenericRelation
from haii.settings import AUTH_USER_MODEL


class Team(models.Model):
    name = models.CharField(verbose_name='نام',max_length=50)

    description = models.TextField(verbose_name='توضیحات')

    image = models.ImageField(verbose_name='لوگو',upload_to=upload_image_path,null=True,blank=True,)

    date = models.DateTimeField(verbose_name='سال ساخت')

    user = models.ManyToManyField(to=AUTH_USER_MODEL,verbose_name='اعضا',related_name='user_team')

    group = GenericRelation('user.CustomGroup', content_type_field='owner_content_type', object_id_field='owner_object_id')

    product = GenericRelation('product.Product', content_type_field='owner_content_type', object_id_field='owner_object_id')


    def __str__(self):
        return self.name


    class Meta:
        app_label = "team"
        verbose_name = 'تیم'
        verbose_name_plural = 'تیم ها'
        base_manager_name = "objects"
        ordering = ['id']