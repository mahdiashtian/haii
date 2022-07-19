from django.db import models
from django.contrib.postgres.fields import HStoreField
from user.models import User


class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    default = models.JSONField()
    information = models.JSONField()
    publish = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + " - publish : " + str(self.publish)

    class Meta:
        verbose_name = 'وقایع'
        verbose_name_plural = 'وقایع ها'
