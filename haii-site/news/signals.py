import json
import os

import redis
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

try:
    r = redis.StrictRedis(host="localhost", port=6379, db=0, password="", decode_responses=True)
except:
    print("[-] i can`t connect to redis!")


@receiver(post_save, sender="news.News")
def run_after_save(instance, sender, created, **kwargs):
    if created:
        if instance.share:
            result = {
                'news': instance.news,
                'image': instance.image.path if instance.image else None,
                'postage_date': str(instance.postage_date),
            }
            data = json.dumps(result)
            r.rpush('sender', data)


@receiver(post_delete, sender="news.News")
def run_after_delete(instance, **kwargs):
    if instance.image:
        path = instance.image.path

        if os.path.exists(path):
            os.remove(path)
