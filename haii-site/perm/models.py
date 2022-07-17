from django.contrib.contenttypes.models import ContentType
from django.contrib.postgres.fields import ArrayField
from django.db import models
from user.models import User


class PermMixin:
    def get_content_type(self, model):
        return str(ContentType.objects.get_for_model(model).id)

    def get_all_perm(self):
        perm_overall = self.perm_overall
        perm_minor = self.perm_minor
        return {'overall': perm_overall, 'minor': perm_minor}

    def has_perm(self, perm, model=None, content_type_id=None, item=None):
        if item:
            item = str(item)
        if model:
            content_type = self.get_content_type(model)
        else:
            content_type = str(content_type_id)
        all_perm = self.get_all_perm()
        overall = all_perm.get('overall', [])
        minor = all_perm.get('minor', {})

        if perm in overall:
            return True
        if content_type and (perm in minor.get(content_type, {}).get(item, [])):
            return True
        return False

    def add_perm(self, perm, model=None, content_type_id=None, item=None):
        if item:
            item = str(item)
        if model:
            content_type = self.get_content_type(model)
        else:
            content_type = str(content_type_id)
        if content_type:
            if not item:
                if perm not in self.perm_overall:
                    self.perm_overall.append(perm)
            else:
                if content_type not in self.perm_minor:
                    self.perm_minor[content_type] = {}
                if perm not in self.perm_minor[content_type].get(item, []):
                    list_perm = self.perm_minor[content_type].get(item, [])
                    list_perm.append(perm)
                    self.perm_minor[content_type][item] = list_perm
            self.save()

    def remove_perm(self, perm, model=None, content_type_id=None, item=None):
        if item:
            item = str(item)
        if model:
            content_type = self.get_content_type(model)
        else:
            content_type = str(content_type_id)
        if content_type:
            if not item:
                if perm in self.perm_overall:
                    self.perm_overall.remove(perm)
            else:
                if content_type not in self.perm_minor:
                    self.perm_minor[content_type] = {}
                if perm in self.perm_minor[content_type].get(item, []):
                    list_perm = self.perm_minor[content_type].get(item, [])
                    list_perm.remove(perm)
                    self.perm_minor[content_type][item] = list_perm
            self.save()


class Perm(models.Model, PermMixin):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, verbose_name='کاربر', related_name='perm_user')
    perm_overall = ArrayField(models.CharField(max_length=100), verbose_name='دسترسی کلی', default=list, blank=True)
    perm_minor = models.JSONField(verbose_name='مجوز های جزئی', default=dict, blank=True)
    creator = models.OneToOneField(to=User, on_delete=models.CASCADE, verbose_name='سازنده',
                                   related_name='perm_creator')

    class Meta:
        verbose_name = 'مجوز'
        verbose_name_plural = 'مجوز ها'

    def __str__(self):
        return self.user.username
