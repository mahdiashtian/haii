from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class User(AbstractUser):

    def get_user_name(self):
        return self.username

content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,verbose_name='مدل')
object_id = models.PositiveIntegerField(verbose_name='آیدی',null=True,blank=True)
content_object = GenericForeignKey('content_type', 'object_id')
overall = models.BooleanField(verbose_name='مجوز کلی',default=False)
creator = models.ForeignKey(User,verbose_name='سازنده',on_delete=models.CASCADE,null=True,blank=True)

Group.add_to_class('content_type',content_type)
Group.add_to_class('object_id',object_id)
Group.add_to_class('content_object',content_object)
Group.add_to_class('overall',overall)
Group.add_to_class('creator',creator)