""" Sales URLs"""

#django
from django.urls import include, path

#rest_framework
from rest_framework.routers import DefaultRouter

#views
from .views import ProductViewSet
from .views import ProductCategoryViewSet
router = DefaultRouter()
router.register(
    r'products',
    ProductViewSet,
    basename='products'
)
router.register(
    r'product_categories',
    ProductCategoryViewSet,
    basename='product_categories'
)
urlpatterns = [
    path('', include(router.urls))
]
