from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def get_user_name(self):
        return self.username