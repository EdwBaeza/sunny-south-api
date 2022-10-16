# Django Rest Framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Models
from sunnysouth.marketplace.models.categories import Category

# Serializers
from sunnysouth.marketplace.serializers.categories import CategoryModelSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
