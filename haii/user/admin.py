from django.contrib import admin
from .models import (
    User
)
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


admin.site.register(User,UserAdmin)