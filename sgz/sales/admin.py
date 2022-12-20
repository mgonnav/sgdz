from django.contrib import admin

from sgz.sales.models import Payment, Sale, SaleDetail


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    pass


@admin.register(SaleDetail)
class SaleDetailAdmin(admin.ModelAdmin):
    pass


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass
