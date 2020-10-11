"""Users URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views.users import UserViewSet
from sunnysouth.sales.views import ProductViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(
    r'users/(?P<username>[a-zA-Z0-9_-]+/products)',
    ProductViewSet,
    basename='users'
)
urlpatterns = [
    path('', include(router.urls))
]
