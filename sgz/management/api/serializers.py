from django.db.models import Sum
from rest_framework import serializers

from sgz.management.models import (
    Allocation,
    PaymentType,
    PointOfSale,
    Product,
    Provider,
    ShoeModel,
    Storeroom,
)


class AllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allocation
        fields = "__all__"


class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = "__all__"


class PointOfSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointOfSale
        fields = "__all__"


class ShoeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeModel
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    shoe_model = ShoeModelSerializer()
    allocations = serializers.SerializerMethodField("get_allocations")
    total_stock = serializers.SerializerMethodField("get_total_stock")

    class Meta:
        model = Product
        fields = "__all__"

    def get_allocations(self, product):
        return {
            allocation.storeroom.name: allocation.stock
            for allocation in product.allocation_set.all()
        }

    def get_total_stock(self, product):
        return product.allocation_set.all().aggregate(Sum("stock"))["stock__sum"]


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = "__all__"


class StoreroomAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allocation
        fields = ("product", "stock")


class StoreroomSerializer(serializers.ModelSerializer):
    allocations = StoreroomAllocationSerializer(read_only=True, many=True)

    class Meta:
        model = Storeroom
        fields = ("name", "allocations")
