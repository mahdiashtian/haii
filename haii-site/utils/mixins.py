from .permissions_ import (
    IsSuperUser,
    IsEditor,
    IsAdder,
    IsRemoval,
    IsViewer,)
from rest_framework.permissions import IsAuthenticated


class PermissiomMixin:
    def get_permissions(self):
            permission_classes = [IsAuthenticated]
            if self.action in ['retrieve','list']:
                permission_classes += [IsSuperUser|IsViewer]

            elif self.action == 'create':
                permission_classes += [IsSuperUser|(IsViewer & IsAdder)]

            elif self.action in ['update','partial_update']:
                permission_classes += [IsSuperUser|(IsViewer & IsEditor)]

            elif self.action == 'destroy':
                permission_classes += [IsSuperUser|(IsViewer & IsRemoval)]

            return [permission() for permission in permission_classes]