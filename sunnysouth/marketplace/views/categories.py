#rest_framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

#models
from sunnysouth.marketplace.models import Category

#serializers
from sunnysouth.marketplace.serializers import CategoryModelSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
