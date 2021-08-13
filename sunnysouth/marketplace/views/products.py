# Django Rest Framework
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.filters import SearchFilter

# Filters
from django_filters.rest_framework import DjangoFilterBackend

# Serializers
from sunnysouth.marketplace.serializers import (
    ProductModelSerializer,
    ProductListSerializer,
    ProductDetailSerializer
)

# Models
from sunnysouth.marketplace.models import Product, User

# Permissions
from sunnysouth.marketplace.permissions.products import IsValidCurrentUser


class ProductViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name', 'price', 'supplier']
    search_fields = ['category__name', 'category__uuid']
    queryset = Product.objects.filter(is_active=True)
    lookup_field = 'uuid'

    def get_serializer_class(self):
        """Get the serializer class depends on the action."""
        if self.action in ['list']:
            return ProductListSerializer
        elif self.action in ['retrieve']:
            return ProductDetailSerializer
