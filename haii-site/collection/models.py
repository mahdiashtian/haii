from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from haii.settings import AUTH_USER_MODEL
from utils.utils import upload_image_path


class BaseField(models.Model):
    name = models.CharField(verbose_name='نام', max_length=50)

    description = models.TextField(verbose_name='توضیحات')

    image = models.ImageField(verbose_name='لوگو', upload_to=upload_image_path, null=True, blank=True, )

    main_job = models.TextField(verbose_name='کار تیم')

    date_of_formation = models.DateTimeField(verbose_name='تاریخ تشکیل', null=True, blank=True)

    user = models.ManyToManyField(to=AUTH_USER_MODEL, verbose_name='اعضا', blank=True)

    product = GenericRelation('product.Product', content_type_field='owner_content_type',
                              object_id_field='owner_object_id')

    class Meta:
        abstract = True


class Startup(BaseField):

    def __str__(self):
        return self.name

    class Meta:
        app_label = "collection"
        verbose_name = 'استارت آپ'
        verbose_name_plural = 'استارت آپ ها'
        base_manager_name = "objects"
        ordering = ['id']


class Team(BaseField):

    def __str__(self):
        return self.name

    class Meta:
        app_label = "collection"
        verbose_name = 'تیم'
        verbose_name_plural = 'تیم ها'
        base_manager_name = "objects"
        ordering = ['id']
