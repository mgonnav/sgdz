from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from sgz.management.api.views import PointOfSaleViewSet, ProviderViewSet
from sgz.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("providers", ProviderViewSet)
router.register("pointsofsale", PointOfSaleViewSet)


app_name = "api"
urlpatterns = router.urls
