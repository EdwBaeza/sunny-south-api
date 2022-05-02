# Django Rest Framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Models
from sunnysouth.marketplace.models.categories import Category

# Serializers
from sunnysouth.marketplace.serializers.categories import CategoryModelSerializer

import time

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer

    # def dispatch(self, request, *args, **kwargs):
    #     time.sleep(10.0)
    #     return super(CategoryViewSet, self).dispatch(request, *args, **kwargs)
