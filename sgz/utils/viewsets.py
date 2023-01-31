from rest_framework.viewsets import ModelViewSet

from sgz.users.permissions import IsOwnerUser
from sgz.utils.mixins import PaginatedCustomOrderingMixin, PartialRetrieveMixin


class BaseSGZViewSet(PartialRetrieveMixin, PaginatedCustomOrderingMixin, ModelViewSet):
    pass


class OwnerSGZViewSet(BaseSGZViewSet):
    permission_classes = [IsOwnerUser]
