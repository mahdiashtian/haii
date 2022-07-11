from rest_framework import viewsets, status
from .serializers_ import UserSerializers, PermissionSerializers, ChangePasswordSerializer
from .models import User
from django.contrib.auth.models import Permission
from utils.permissions_ import IsSuperUser
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.all()
    permission_classes = [IsSuperUser]

    def get_serializer_class(self):
        serializer_class = UserSerializers
        if self.action == 'update':
            serializer_class.Meta.read_only_fields = ['password']
        else:
            serializer_class.Meta.read_only_fields = []
        return serializer_class

    @action(detail=True, methods=['put'])
    def chnage_password(self, request, pk=None):
        user = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data['new_password']
            user.set_password(password)
            user.save()
            return Response({
                'status': 'success',
                'message': 'Password changed successfully',
                'password': password,
            })
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class PermissionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PermissionSerializers
    queryset = Permission.objects.all()
    permission_classes = [IsSuperUser]
