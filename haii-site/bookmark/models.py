from django.db import models


class BaseField(models.Model):
    name = models.CharField(verbose_name='نام', max_length=50)

    class Meta:
        abstract = True


class Tag(BaseField):
    def __str__(self):
        return self.name

    class Meta:
        app_label = "bookmark"
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'
        base_manager_name = "objects"
        ordering = ['id']


class Category(BaseField):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "bookmark"
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        base_manager_name = "objects"
        ordering = ['id']
