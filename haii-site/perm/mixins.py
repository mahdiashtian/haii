from rest_framework.permissions import IsAuthenticated

from .permission_ import (
    IsSuperUser,
    IsEditor,
    IsAdder,
    IsRemoval,
    IsViewer
)


class PermissionMixin:
    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        if self.action in ['list', 'retrieve']:
            permission_classes += [IsSuperUser | IsViewer]

        elif self.action == 'create':
            permission_classes += [IsSuperUser | IsAdder]

        elif self.action in ['update', 'partial_update']:
            permission_classes += [IsSuperUser | IsEditor]

        elif self.action == 'destroy':
            permission_classes += [IsSuperUser | IsRemoval]

        return [permission() for permission in permission_classes]
