"""Suppliers URLs"""
#django
from django.urls import include, path

#rest_framework
from rest_framework.routers import DefaultRouter

#views
from .views import ManufacturerViewSet

router = DefaultRouter()
router.register(
    r'suppliers',
    ManufacturerViewSet,
    basename='suppliers'
)

urlpatterns = [
    path('', include(router.urls))
]
