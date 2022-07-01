from django.db import models
from utils.utils import upload_image_path
from django.conf import settings


class Startup(models.Model):
    name = models.CharField(verbose_name='نام',max_length=50)

    description = models.TextField(verbose_name='توضیحات',blank=True,null=True)

    image = models.ImageField(verbose_name='لوگو',upload_to=upload_image_path,null=True,blank=True)

    main_job = models.TextField(verbose_name='کار استارت آپ')

    date_of_formation = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ تشکیل')

    ceo = models.ForeignKey(to=settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,related_name='ceo_team',null=True,blank=True)

    
    def __str__(self):
        return self.name

    
    class Meta:
        app_label = "startup"
        verbose_name = 'استارت آپ'
        verbose_name_plural = 'استارت آپ ها'
        base_manager_name = "objects"
        ordering = ['id']