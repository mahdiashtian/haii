from tokenize import group
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, PermissionsMixin
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError


class User(AbstractUser):
    def is_group(self, group):
        result = self.groups.filter(name=group).exists()
        return result


limit = models.Q(app_label='startup', model='startup') | models.Q(app_label='team', model='team') | models.Q(
    app_label='product', model='product')

owner_content_type = models.ForeignKey(ContentType,
                                       on_delete=models.CASCADE,
                                       related_name="owner_group_content_type",
                                       limit_choices_to=limit, )

owner_object_id = models.PositiveIntegerField(blank=True,null=True)

owner_instance = GenericForeignKey('owner_content_type', 'owner_object_id')

is_admin = models.BooleanField(default=False)

creator = models.ForeignKey(User,on_delete=models.CASCADE)

def clean(self):
    print(self.is_admin)
    result = self.owner_content_type.model_class().objects.filter(id=self.owner_object_id).exists()
    if not self.is_admin and not result:
        raise ValidationError(dict(owner_object_id=_('هیچ آیتمی با این آیدی وجود ندارد.')))


Group.clean = clean
Group.add_to_class('is_admin', is_admin)
Group.add_to_class('creator',creator)
Group.add_to_class('owner_content_type', owner_content_type)
Group.add_to_class('owner_object_id', owner_object_id)
Group.add_to_class('owner_instance', owner_instance)