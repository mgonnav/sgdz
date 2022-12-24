from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from sgz.management.models import (
    Allocation,
    Brand,
    Color,
    PaymentType,
    PointOfSale,
    Product,
    Provider,
    ShoeModel,
    Storeroom,
)
from sgz.users.permissions import IsOwnerUser

from .serializers import (
    AllocationSerializer,
    BrandSerializer,
    ColorSerializer,
    PaymentTypeSerializer,
    PointOfSaleSerializer,
    ProductCreateUpdateSerializer,
    ProductSerializer,
    ProviderSerializer,
    ShoeModelSerializer,
    StoreroomSerializer,
)


class AllocationViewSet(ModelViewSet):
    serializer_class = AllocationSerializer
    queryset = Allocation.objects.all()
    permission_classes = [IsOwnerUser]


class PaymentTypeViewSet(ModelViewSet):
    """
    CRUD for points of sale
    Related use case: CU-09
    """

    serializer_class = PaymentTypeSerializer
    queryset = PaymentType.objects.all()
    permission_classes = [IsOwnerUser]
    lookup_field = "name"


class PointOfSaleViewSet(ModelViewSet):
    """
    CRUD for points of sale
    Related use case: CU-07
    """

    serializer_class = PointOfSaleSerializer
    queryset = PointOfSale.objects.all()
    permission_classes = [IsOwnerUser]
    lookup_field = "name"


class ProductViewSet(ModelViewSet):
    """
    CRUD for points of sale
    Related use case: CU-12
    """

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsOwnerUser]
    lookup_field = "pk"

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return ProductCreateUpdateSerializer
        return self.serializer_class


class ProviderViewSet(ModelViewSet):
    """
    CRUD for providers.
    Related use case: CU-06
    """

    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()
    permission_classes = [IsOwnerUser]
    lookup_field = "contact_name"


class BrandViewSet(ModelViewSet):
    """
    CRUD for points of sale
    Related use case: CU-11
    """

    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    permission_classes = [IsOwnerUser]
    lookup_field = "name"


class ColorViewSet(ModelViewSet):
    """
    CRUD for points of sale
    Related use case: CU-11
    """

    serializer_class = ColorSerializer
    queryset = Color.objects.all()
    permission_classes = [IsOwnerUser]
    lookup_field = "name"


class ShoeModelViewSet(ModelViewSet):
    """
    CRUD for points of sale
    Related use case: CU-11
    """

    serializer_class = ShoeModelSerializer
    queryset = ShoeModel.objects.all()
    permission_classes = [IsOwnerUser]
    lookup_field = "code"

    def retrieve(self, request, code=""):
        shoe_models = self.queryset.filter(code__icontains=code)
        serializer = self.serializer_class(shoe_models, many=True)
        return Response(serializer.data[:10])


class StoreroomViewSet(ModelViewSet):
    """
    CRUD for points of sale
    Related use case: CU-08
    """

    serializer_class = StoreroomSerializer
    queryset = Storeroom.objects.all()
    permission_classes = [IsOwnerUser]
    lookup_field = "name"
