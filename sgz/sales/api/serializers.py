from rest_framework import serializers

from sgz.management.api.serializers import (
    AllocationSerializer,
    PaymentTypeSerializer,
    PointOfSaleSerializer,
)
from sgz.sales.models import Payment, Sale, SaleDetail
from sgz.users.api.serializers import UserSerializer


class SaleDetailSerializer(serializers.ModelSerializer):
    """
    CRUD for sale
    Related use cases: CU-03, CU-04, CU-05
    """

    allocation = AllocationSerializer()

    class Meta:
        model = SaleDetail
        fields = ("id", "allocation", "price", "number_of_units")


class SaleDetailCreateSerializer(serializers.ModelSerializer):
    """
    Sale creation
    Related use cases: CU-03
    """

    class Meta:
        model = SaleDetail
        fields = ("price", "number_of_units", "allocation")


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

    details = SaleDetailCreateSerializer(many=True)

    class Meta:
        model = Sale
        fields = ("user", "point_of_sale", "details")
        extra_kwargs = {"details": {"write_only": True}}

    def create(self, validated_data):
        details = validated_data.pop("details")
        sale = Sale.objects.create(**validated_data)
        for detail in details:
            if detail.get("allocation").stock < detail.get("number_of_units"):
                serializers.ValidationError(
                    f"No hay suficiente stock del producto {detail.get('allocation').product.code} en el almacén "
                    f"{detail.get('allocation').warehouse.name} para realizar la venta."
                )

            sale_detail = SaleDetail.objects.create(**detail, sale=sale)
            sale_detail.allocation.stock -= sale_detail.number_of_units
            sale_detail.allocation.save()
        return sale


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
