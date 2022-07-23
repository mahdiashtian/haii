from rest_framework.permissions import IsAuthenticated

from .permission_ import (
    IsSuperUser,
    IsEditor,
    IsAdder,
    IsRemoval,
    IsListViewer,
    IsRetrieveView
)


class PermissionMixin:
    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        if self.action == 'list':
            permission_classes += [IsSuperUser | IsListViewer]
            
        if self.action == 'retrieve':
            permission_classes += [IsSuperUser | IsRetrieveView]

        elif self.action == 'create':
            permission_classes += [IsSuperUser | IsAdder]

        elif self.action in ['update', 'partial_update']:
            permission_classes += [IsSuperUser | IsEditor]

        elif self.action == 'destroy':
            permission_classes += [IsSuperUser | IsRemoval]

        return [permission() for permission in permission_classes]
