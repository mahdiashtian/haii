from django.db import models
from django.contrib.auth.models import AbstractUser , Group
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError


class CustomGroup(Group):
    limit = models.Q(app_label = 'startup', model = 'startup') | models.Q(app_label = 'team', model = 'team')
    owner_content_type = models.ForeignKey(ContentType,
        on_delete=models.CASCADE, 
        related_name="team_content_type",
        null=True,blank=True,
        limit_choices_to = limit)
    owner_object_id = models.PositiveIntegerField(null=True,blank=True)
    owner_instance = GenericForeignKey('owner_content_type', 'owner_object_id')


    def clean(self):
        if not self.owner_content_type.model_class().objects.filter(id=self.owner_object_id).exists():
            raise ValidationError({'owner_object_id': _('هیچ آیتمی با این آیدی وجود ندارد.')})


    def __str__(self):
        return f"{self.name} | {self.owner_content_type.model_class().objects.filter(id=self.owner_object_id).first().name}"


    class Meta:
        verbose_name = _("group")
        verbose_name_plural = _("groups")


class User(AbstractUser):
    groups = models.ManyToManyField(
        CustomGroup,
        verbose_name=_("groups"),
        blank=True,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_name="user_set",
        related_query_name="user",
    )


    def is_group(self,group):
        result = self.groups.filter(name=group).exists()
        return result