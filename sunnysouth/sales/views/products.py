""" views products. """

#django rest_framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

#serializers
from sunnysouth.sales.serializers import ProductModelSerializer, ProductListSerializer

#filters
from django_filters.rest_framework import DjangoFilterBackend

#models
from sunnysouth.sales.models import Product
from sunnysouth.users.models import User

class ProductViewSet(
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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'price', 'supplier']


    def dispatch(self, request, *args, **kwargs):
        """Verify that the user exists, active and verified."""
        username = kwargs['username']
        self.user = get_object_or_404(User, username=username)
        return super(ProductViewSet, self).dispatch(request, *args, **kwargs)

    def get_serializer_class(self):
        """ Get the serializer class depends on the action."""
        if self.action in ['list', 'supplier']:
            return ProductListSerializer
        else:
            return ProductModelSerializer

    def get_queryset(self):
        """Get queryset for products."""
        if self.action == "supplier":
            return Product.objects.filter(
                supplier__user__username=self.kwargs['pk'],
                supplier__user__is_verified=True,
            )
        else:
            return Product.objects.filter(is_active=True)

    def list(self, request, *args, **kwargs):
        return super(ProductViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """ create product. """
        request.data['supplier'] = request.user.id
        return super(ProductViewSet, self).create(request, *args, **kwargs)

    # def perfom_create(self, serializer);
    #     """ Assign current user as provider."""


    @action(detail=True, methods=['GET'])
    def supplier(self, request, *args, **kwargs):
        """ Get products by supplier"""
        return self.list(request, *args, **kwargs)



