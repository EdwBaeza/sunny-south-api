""" Category views. """

#rest_framework
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
#models
from sunnysouth.sales.models import Category

#serializers
from sunnysouth.sales.serializers import CategoryModelSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
