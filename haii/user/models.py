from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def is_group(self,group):
        result = self.groups.filter(name=group).exists()
        return result