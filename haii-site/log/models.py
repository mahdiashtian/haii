from django.db import models
from user.models import User


class Log(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    information = models.JSONField()
    publish = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'وقایع'
        verbose_name_plural = 'وقایع ها'