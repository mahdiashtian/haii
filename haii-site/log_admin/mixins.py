from rest_framework.response import Response
from rest_framework.status import HTTP_409_CONFLICT, HTTP_202_ACCEPTED

from .models import Log


class LogAdminMixin:
    def update(self, request, *args, **kwargs):
        user = self.request.user
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        if user.is_superuser:
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        else:
            data = serializer.initial_data.copy().dict()
            default = serializer.initial_data.copy().dict()
            item = dict(serializer.data.items())
            data['model'] = self.model.__name__.lower()
            data['app_label'] = self.model._meta.app_label
            date_ = {k: v for k, v in data.items() if v}
            item.update(date_)
            query = Log.objects.filter(information__id=item['id'], information__app_label=data['app_label'],
                                       information__model=data['model'], publish=False)
            if not query.exists():
                Log.objects.create(user=user, information=item, default=default)
                return Response(data={"detail": "تنظیمات اعمال شده بعد از تایید ادمین نمایش داده خواهند شد"},
                                status=HTTP_202_ACCEPTED)
            return Response(data={"detail": "شما از قبل یک درخواست اپدیت دارید!"},
                            status=HTTP_409_CONFLICT)
