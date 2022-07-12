from rest_framework import viewsets
from .models import Team
from .serializers_ import TeamSerializers
from log.models import Log
from rest_framework.response import Response
from rest_framework.status import HTTP_202_ACCEPTED,HTTP_409_CONFLICT
from utils.mixins import PermissionMixin


class TeamViewSet(PermissionMixin,viewsets.ModelViewSet):
    serializer_class = TeamSerializers
    model = Team
    queryset = Team.objects.all()

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
            item = dict(serializer.data.items())
            data['model'] = self.model.__name__.lower()
            data['app_label'] = self.model._meta.app_label
            item.update(data)
            query = Log.objects.filter(information__id=item['id'])
            if not query.exists():
                Log.objects.create(user=user, information=item)
                return Response(data={"detail": "تنظیمات اعمال شده بعد از تایید ادمین نمایش داده خواهند شد"},
                                  status=HTTP_202_ACCEPTED)
            return Response(data={"detail": "شما از قبل یک درخواست اپدیت دارید!"},
                              status=HTTP_409_CONFLICT)
