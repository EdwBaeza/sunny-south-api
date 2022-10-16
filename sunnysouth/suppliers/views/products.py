# Django Rest Framework
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404

# Filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

# Serializers
from sunnysouth.marketplace.serializers import (
    ProductModelSerializer,
    ProductListSerializer,
    ProductDetailSerializer
)

# Models
from sunnysouth.marketplace.models import Product, Supplier

# Permissions
from sunnysouth.marketplace.permissions.products import IsValidCurrentUser


class ProductViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name', 'price']
    search_fields = ['category__name', 'category__uuid']
    lookup_field = 'uuid'

    def dispatch(self, request, *args, **kwargs):
        self.supplier = get_object_or_404(Supplier, uuid=kwargs['supplier_id'])
        return super(ProductViewSet, self).dispatch(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action in ['list']:
            return ProductListSerializer
        elif self.action in ['retrieve']:
            return ProductDetailSerializer
        else:
            return ProductModelSerializer

    def get_permissions(self):
        permissions = [IsAuthenticated]
        return [p() for p in permissions]

    def get_queryset(self):
        return Product.objects.filter(is_active=True, supplier=self.supplier)

    def get_serializer_context(self):
        context = {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

        if self.action in ['create', 'update', 'partial_update']:
            context['supplier'] = self.user.profile

        return context
