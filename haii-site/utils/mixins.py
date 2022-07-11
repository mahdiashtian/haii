from .permissions_ import (
    IsSuperUser,
    IsEditor,
    IsAdder,
    IsRemoval,
    IsViewer, )
from rest_framework.permissions import IsAuthenticated


class PermissiomMixin:
    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        if self.action == 'create':
            permission_classes += [IsSuperUser | IsAdder]

        elif self.action in ['update', 'partial_update']:
            permission_classes += [IsSuperUser | IsEditor]

        elif self.action == 'destroy':
            permission_classes += [IsSuperUser | IsRemoval]

        return [permission() for permission in permission_classes]
