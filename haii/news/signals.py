from django.dispatch import receiver
from django.db.models.signals import post_delete , post_save
import os
import json
import redis


try:
	r = redis.StrictRedis(host = "localhost",port = 6379,db = 1,password = "",decode_responses=True)
except:
    print("[-] i can`t connect to redis!")



@receiver(post_save,sender="news.News")
def run_after_save(instance,**kwargs):
    if instance.share:
        result = {
            'news':instance.news,
            'image':instance.image.url if instance.image else None,
            'date_of_send':str(instance.date_of_send),

        }
        data = json.dumps(result)
        r.rpush('sender',data)


@receiver(post_delete,sender="news.News")
def run_after_delete(instance,**kwargs):
    
    if instance.image:
        path = instance.image.path

        if os.path.exists(path):
            os.remove(path)