from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_team_manager = models.BooleanField(verbose_name='مدیر تیم',default=False)

    is_editor = models.BooleanField(verbose_name='ویرایشگر',default=False)