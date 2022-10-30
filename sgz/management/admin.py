from django.contrib import admin

from sgz.management.models import PointOfSale, Provider


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    pass


@admin.register(PointOfSale)
class PointOfSaleAdmin(admin.ModelAdmin):
    pass
