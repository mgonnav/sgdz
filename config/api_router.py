from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from sgz.management.api.views import (
    AllocationViewSet,
    PaymentTypeViewSet,
    PointOfSaleViewSet,
    ProductViewSet,
    ProviderViewSet,
    ShoeModelViewSet,
    StoreroomViewSet,
)
from sgz.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("allocations", AllocationViewSet)
router.register("paymenttypes", PaymentTypeViewSet)
router.register("pointsofsale", PointOfSaleViewSet)
router.register("products", ProductViewSet)
router.register("providers", ProviderViewSet)
router.register("shoemodels", ShoeModelViewSet)
router.register("storerooms", StoreroomViewSet)


app_name = "api"
urlpatterns = router.urls
