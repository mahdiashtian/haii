from django.db import models
from user.models import User


class Perm(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='کاربر')
    perm_overall = models.JSONField(verbose_name='مجوز های کلی')
    perm_minor = models.JSONField(verbose_name='مجوز های جزئی')

    class Meta:
        verbose_name = 'مجوز'
        verbose_name_plural = 'مجوز ها'
