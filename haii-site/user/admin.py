from django.contrib import admin
from .models import (
    User,
)
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group


admin.site.register(User,UserAdmin)