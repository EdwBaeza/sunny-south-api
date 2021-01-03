""" Category views. """

#rest_framework
from rest_framework import viewsets, mixins, status

#models
from sunnysouth.sales.models import Category

#serializers
from sunnysouth.sales.serializers import CategoryModelSerializer

class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
