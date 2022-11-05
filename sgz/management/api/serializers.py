from rest_framework import serializers

from sgz.management.models import (
    PaymentType,
    PointOfSale,
    Product,
    Provider,
    ShoeModel,
    Storeroom,
)


class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = "__all__"


class PointOfSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointOfSale
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = "__all__"


class ShoeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeModel
        fields = "__all__"


class StoreroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storeroom
        fields = "__all__"
