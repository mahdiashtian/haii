from django.db import models
from utils.utils import upload_image_path


class Slider(models.Model):
    image = models.ImageField(verbose_name='تصویر',upload_to=upload_image_path,null=True,blank=True,)
    description = models.CharField(verbose_name='توضیحات',max_length=250)
    active = models.BooleanField(default=True)


    class Meta:
        app_label = 'slider'
        verbose_name = "اسلایدر"
        verbose_name_plural = "اسلایدر ها"