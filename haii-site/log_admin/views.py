from rest_framework import mixins
from rest_framework import viewsets

from .models import Log
from .serializers_ import LogSerializers


class LogViewSet(
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.ListModelMixin,
                 viewsets.GenericViewSet):
    serializer_class = LogSerializers
    queryset = Log.objects.all()
    model = Log
