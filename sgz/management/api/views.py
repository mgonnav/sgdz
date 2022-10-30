from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from sgz.management.models import PointOfSale, Provider

from .serializers import PointOfSaleSerializer, ProviderSerializer


class ProviderViewSet(ModelViewSet):
    """
    CRUD for providers.
    Related use case: CU-06
    """

    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()
    permission_classes = [IsAdminUser]
    lookup_field = "contact_name"


class PointOfSaleViewSet(ModelViewSet):
    """
    CRUD for points of sale
    Related use case: CU-07
    """

    serializer_class = PointOfSaleSerializer
    queryset = PointOfSale.objects.all()
    permission_classes = [IsAdminUser]
    lookup_field = "name"
