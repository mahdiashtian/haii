from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q


@receiver(post_save, sender="log.Log")
def run_after_change(sender, instance, created, **kwargs):
    if not created:
        publish = instance.publish
        if publish:
            data = instance.information
            user = data.pop('user')
            limit = Q(app_label=data.pop('app_label'), model=data.pop('model'))
            content_type = ContentType.objects.filter(limit).first()
            if content_type:
                model_obj = content_type.model_class()
                obj = model_obj.objects.filter(id=data['id'])
                obj.update(**data)
                instance_obj = obj.first()
                instance_obj.user.set(user)
                if getattr(instance_obj, '_prefetched_objects_cache', None):
                    instance_obj._prefetched_objects_cache = {}
        instance.delete()
