from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from user.models import User
from perm.models import Perm


@receiver(post_save, sender=User)
def create_user_permission(sender, instance, created, **kwargs):
    if created:
        Perm.objects.create(user=instance)