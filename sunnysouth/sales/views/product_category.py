""" Product Category views."""

#rest_framework
from rest_framework import viewsets, mixins, status

#models
from sunnysouth.sales.models import ProductCategory

#serializers
from sunnysouth.sales.serializers import ProductCategoryModelSerializer

class ProductCategoryViewSet(viewsets.ModelViewSet):
    
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategoryModelSerializer