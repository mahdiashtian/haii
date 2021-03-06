import os

from django.db.models.signals import post_delete
from django.dispatch import receiver


@receiver(post_delete, sender="collection.Startup")
def run_after_delete(instance, **kwargs):
    if instance.image:
        path = instance.image.path

        if os.path.exists(path):
            os.remove(path)


@receiver(post_delete, sender="collection.Team")
def run_after_delete(instance, **kwargs):
    if instance.image:
        path = instance.image.path

        if os.path.exists(path):
            os.remove(path)
