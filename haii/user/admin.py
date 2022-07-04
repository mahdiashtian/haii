from django.contrib import admin
from .models import (
    User,
    CustomGroup
)
from django.contrib.auth.admin import UserAdmin , GroupAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group


admin.site.unregister(Group)
admin.site.register(CustomGroup,GroupAdmin)
admin.site.register(User,UserAdmin)