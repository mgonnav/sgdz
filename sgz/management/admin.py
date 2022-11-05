from django.contrib import admin

from sgz.management.models import (
    PaymentType,
    PointOfSale,
    Product,
    Provider,
    ShoeModel,
    Storeroom,
)


@admin.register(PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(PointOfSale)
class PointOfSaleAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    pass


@admin.register(ShoeModel)
class ShoeModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Storeroom)
class StoreroomAdmin(admin.ModelAdmin):
    pass
