from bookmark.models import Tag, Category
from django.db import models
from utils.utils import upload_image_path


class News(models.Model):
    name = models.CharField(verbose_name='نام', max_length=50)

    news = models.TextField(verbose_name='خبر')

    image = models.ImageField(verbose_name='تصویر', upload_to=upload_image_path, blank=True, null=True)

    date_of_registration = models.DateTimeField('تاریخ ثبت', auto_now_add=True)

    edit_date = models.DateTimeField('تاریخ ویرایش', auto_now=True)

    share = models.BooleanField(verbose_name='اشتراک گذاری در شبکه های اجتماعی', default=False)

    postage_date = models.DateTimeField('تاریخ ارسال به شبکه های اجتماعی', blank=True, null=True)

    tag = models.ManyToManyField(Tag, verbose_name='تگ', blank=True)

    category = models.ManyToManyField(Category, verbose_name='دسته بندی', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "news"
        verbose_name = 'خبر'
        verbose_name_plural = 'خبر ها'
        base_manager_name = "objects"
        ordering = ['date_of_registration']
