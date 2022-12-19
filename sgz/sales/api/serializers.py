from rest_framework import serializers

from sgz.management.api.serializers import (
    PaymentTypeSerializer,
    PointOfSaleSerializer,
    ProductSerializer,
)
from sgz.sales.models import Payment, Sale, SaleDetail
from sgz.users.api.serializers import UserSerializer


class SaleDetailSerializer(serializers.ModelSerializer):
    """
    CRUD for sale
    Related use cases: CU-03, CU-04, CU-05
    """

    product = ProductSerializer()

    class Meta:
        model = SaleDetail
        fields = ("id", "price", "number_of_units", "product")


class SaleDetailCreateSerializer(serializers.ModelSerializer):
    """
    Sale creation
    Related use cases: CU-03
    """

    class Meta:
        model = SaleDetail
        fields = ("price", "number_of_units", "product")


class SaleSerializer(serializers.ModelSerializer):
    """
    CRUD for sale
    Related use cases: CU-03, CU-04, CU-05
    """

    point_of_sale = PointOfSaleSerializer()
    user = UserSerializer()

    class Meta:
        model = Sale
        fields = "__all__"
        read_only_fields = ("full_sale_price",)


class SaleCreateSerializer(serializers.ModelSerializer):
    """
    CRUD for sale
    Related use cases: CU-03, CU-04, CU-05
    """

    class Meta:
        model = Sale
        fields = ("user", "point_of_sale")


class PaymentSerializer(serializers.ModelSerializer):
    """
    CRUD for sale
    Related use cases: CU-03
    """

    payment_type = PaymentTypeSerializer()

    class Meta:
        model = Payment
        fields = "__all__"


class PaymentCreateSerializer(serializers.ModelSerializer):
    """
    Sale creation
    Related use cases: CU-03
    """

    class Meta:
        model = Payment
        fields = ("payment_type", "amount", "operation_code")
