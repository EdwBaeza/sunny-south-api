"""Marketplace URLs"""
# Django
from django.urls import include, path

# Django Rest Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import ProductViewSet, CategoryViewSet, UserViewSet, MeAPIView, AssetAPIView

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

urlpatterns = [
    path('', include(router.urls)),
    path('users/me', MeAPIView.as_view(), name='users-me'),
    path(r'assets', AssetAPIView.as_view(), name='asset')
]
