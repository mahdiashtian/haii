from django.db import models
from utils.utils import upload_image_path


class BaseField(models.Model):
    name = models.CharField(verbose_name='نام',max_length=50)


    class Meta:
        abstract = True


class Tag(BaseField):
    def  __str__(self):
        return self.name


    class Meta:
        app_label = "news"
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'
        base_manager_name = "objects"
        ordering = ['id']


class Category(BaseField):
    parent = models.ForeignKey('self',on_delete=models.CASCADE)


    def  __str__(self):
        return self.name


    class Meta:
        app_label = "news"
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        base_manager_name = "objects"
        ordering = ['id']


class News(BaseField):
    news = models.TextField(verbose_name='خبر')

    image = models.ImageField(verbose_name='تصویر',upload_to=upload_image_path)

    date_of_registration = models.DateTimeField('تاریخ ثبت',auto_now_add=True)

    edit_date = models.DateTimeField('تاریخ ویرایش',auto_now=True)

    share = models.BooleanField(verbose_name='اشتراک گذاری در شبکه های اجتماعی',default=False)

    tag = models.ManyToManyField(Tag,verbose_name='تگ',blank=True)

    category = models.ManyToManyField(Category,verbose_name='دسته بندی',blank=True)


    class Meta:
        app_label = "news"
        verbose_name = 'خبر'
        verbose_name_plural = 'خبر ها'
        base_manager_name = "objects"
        ordering = ['date_of_registration']