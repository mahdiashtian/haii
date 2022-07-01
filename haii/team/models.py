from django.db import models
from utils.utils import upload_image_path


class BaseField(models.Model):
    name = models.CharField(verbose_name='نام',max_length=50)

    description = models.TextField(verbose_name='توضیحات')

    image = models.ImageField(verbose_name='لوگو',upload_to=upload_image_path,null=True,blank=True,)

    date = models.DateTimeField(auto_now_add=True,verbose_name='سال ساخت')

    
    class Meta:
        abstract = True


class Product(BaseField):
    def __str__(self):
        return self.name


    class Meta:
        app_label = "team"
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
        base_manager_name = "objects"
        ordering = ['date']



class Team(BaseField):
    product = models.ManyToManyField(to=Product,related_name='product_team',blank=True)


    def __str__(self):
        return self.name


    class Meta:
        app_label = "team"
        verbose_name = 'تیم'
        verbose_name_plural = 'تیم ها'
        base_manager_name = "objects"
        ordering = ['id']