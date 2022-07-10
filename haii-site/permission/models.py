from django.db import models
from django.contrib.postgres.fields import HStoreField
from user.models import User


def default():
    return {
        "product": [
            {

            },
        ],
        "startup": [
            {

            },
        ],
        "team": [
            {

            },
        ]
    }


class Permission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    perm = HStoreField(default=default)

    class Meta:
        verbose_name = 'مجوز'
        verbose_name_plural = 'مجوز ها'

    def __str__(self):
        return self.user.username
