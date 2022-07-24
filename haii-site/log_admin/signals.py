from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.utils import model_meta


@receiver(post_save, sender="log_admin.Log")
def run_after_change(sender, instance, created, **kwargs):
    if not created:
        publish = instance.publish
        if publish:
            data = instance.information
            limit = Q(app_label=data.pop('app_label',None), model=data.pop('model',None))
            content_type = ContentType.objects.filter(limit).first()
            if content_type:
                instance_ = content_type.model_class().objects.get(id=data['id'])
                info = model_meta.get_field_info(instance_)
                m2m_fields = []
                new_data = {k: True if data[k] == 'true' else False if data[k] == 'false' else data[k] for k in data}
                for attr, value in new_data.items():
                    if attr in info.relations and info.relations[attr].to_many:
                        m2m_fields.append((attr, value))
                    elif attr in info.relations and info.relations[attr]:
                        setattr(instance_, attr+".id", int(value))
                    else:
                        setattr(instance_, attr, value)
                instance_.save()
                for attr, value in m2m_fields:
                    field = getattr(instance_, attr)
                    field.set(value)
                if getattr(instance_, '_prefetched_objects_cache', None):
                    instance_._prefetched_objects_cache = {}
            else:
                instance.delete()