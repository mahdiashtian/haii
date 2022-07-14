from django.db import models
from user.models import User


class Permission(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='کاربر')
    perm = models.JSONField(verbose_name='مجوز ها')

    class Meta:
        verbose_name = 'مجوز'
        verbose_name_plural = 'مجوز ها'
