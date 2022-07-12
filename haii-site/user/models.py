from tokenize import group
from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import HStoreField
from django.contrib.contenttypes.models import ContentType
import ast


def default():
    return {

    }


class PermissionMixin:
    def has_perm_custom_(self, dict_, content_type=None, id=None, perm=None):
        key, value = dict_
s        if key == 'overall':
            if perm in value:
                return True
        elif key == str(content_type):
            value = value.get(str(id), None)
            if value and perm in value:
                return True
        return False

    def has_perm_custom(self, perm=None, model=None, id=None):
        all_perm = self.get_all_perm_user()
        print(all_perm.items())
        content_type = self.get_content_type(model)
        func = dict(filter(lambda dict_: self.has_perm_custom_(dict_, content_type=content_type.id, id=id, perm=perm),
                           all_perm.items()))
        if func:
            return True
        return False


class ToolsPermissionMixin:
    def to_dict(self, value=None):
        if value is None:
            value = self.perm
        new_value = {}
        if getattr(value, 'items', None):
            for i, x in value.items():
                if isinstance(x, str):
                    x = ast.literal_eval(x)
                    self.to_dict(value=x)
                new_value[i] = x
        return new_value

    def to_str(self):
        new_value = {}
        for i, x in self.perm.items():
            new_value[i] = str(x)
        return new_value

    def get_all_perm_user(self):
        all_perm = self.to_dict()
        return all_perm


class User(AbstractUser, ToolsPermissionMixin, PermissionMixin):
    perm = HStoreField(default=default, verbose_name='دسترسی ها')

    def get_content_type(self, model):
        content_type = ContentType.objects.get_for_model(model)
        return content_type
