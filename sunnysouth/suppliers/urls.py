"""Suppliers URLs"""
# django
from django.urls import include, path

# rest_framework
from rest_framework.routers import DefaultRouter

# views
from .views import ProductViewSet, SupplierViewSet

router = DefaultRouter()
router.register(
    r'suppliers',
    SupplierViewSet,
    basename='suppliers'
)

router.register(
    r'suppliers/(?P<supplier_id>[^/.]+)/products',
    ProductViewSet,
    basename='supplier-products'
)

urlpatterns = [
    path('', include(router.urls))
]
