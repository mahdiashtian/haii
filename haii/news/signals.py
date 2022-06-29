from django.dispatch import receiver
from django.db.models.signals import post_delete
import os


@receiver(post_delete,sender="news.News")
def run_after_delete(instance,**kwargs):
    
    if instance.image:
        path = instance.image.path

        if os.path.exists(path):
            os.remove(path)


