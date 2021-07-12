"""Marketplace URLs"""
#django
from django.urls import include, path

#rest_framework
from rest_framework.routers import DefaultRouter

#views
from .views import ProductViewSet
from .views import CategoryViewSet
from .views import UserViewSet
from .views import ProductUserViewSet

router = DefaultRouter()
router.register(
    r'products',
    ProductViewSet,
    basename='products'
)
router.register(
    r'categories',
    CategoryViewSet,
    basename='categories'
)
router.register(r'users', UserViewSet, basename='users')
router.register(
    r'users/(?P<username>[^/.]+)/products',
    ProductUserViewSet,
    basename='users-products'
)

urlpatterns = [
    path('', include(router.urls))
]
