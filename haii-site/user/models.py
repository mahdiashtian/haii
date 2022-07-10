from tokenize import group
from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class User(AbstractUser):
    def is_group(self, group):
        result = self.groups.filter(name=group).exists()
        return result