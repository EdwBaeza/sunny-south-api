""" views products. """

#django rest_framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.filters import SearchFilter

#serializers
from sunnysouth.marketplace.serializers import ProductModelSerializer, ProductListSerializer, ProductDetailSerializer
from sunnysouth.marketplace.serializers.categories import CategoryModelSerializer

#filters
from django_filters.rest_framework import DjangoFilterBackend

#models
from sunnysouth.marketplace.models import Product, Category
from sunnysouth.marketplace.models import User

#Permissions
from sunnysouth.marketplace.permissions.products import IsValidCurrentUser

class ProductUserViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
    ):
    """
        Handle crud for products
    """
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name', 'price', 'supplier']
    search_fields = ['category__name', 'category__uuid']
    queryset = Product.objects.filter(is_active=True)
    lookup_field = 'uuid'

    def dispatch(self, request, *args, **kwargs):
        """Verify that the user exists, active and verified."""
        username = kwargs['username']
        self.user = get_object_or_404(
            User,
            username=username,
            is_active=True,
            is_verified=True
        )
        return super(ProductUserViewSet, self).dispatch(request, *args, **kwargs)

    def get_serializer_class(self):
        """Get the serializer class depends on the action."""
        if self.action in ['list']:
            return ProductListSerializer
        elif self.action in ['retrieve']:
            return ProductDetailSerializer
        else:
            return ProductModelSerializer

    def get_permissions(self):
        permissions = [IsAuthenticated]
        if self.action in ['update', 'partial_update', 'create', 'destroy']:
            permissions+= [IsValidCurrentUser]
        return [p() for p in permissions ]

    def get_queryset(self):
        """Get queryset for products."""
        return Product.objects.filter(is_active=True, supplier=self.user.profile)

    def get_serializer_context(self):
        """Extra context provided to the serializer class."""
        context = {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

        if self.action in ['create', 'update', 'partial_update']:
            context['supplier'] = self.user.profile

        return context

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
