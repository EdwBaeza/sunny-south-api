""" Products serializers."""

#django
from django.conf import settings
from django.contrib.auth import authenticate

#rest_framework
from rest_framework import serializers

# #serializers

# from genericsl_django.sales.serializers import ProductCategoryModelSerializer

#models
from genericsl_django.sales.models import Product


class ProductModelSerializer(serializers.ModelSerializer):
    """ Product Model Serializer"""
    #product_category = serializers.StringRelatedField()
    #picture = serializers.ImageField(required=None)
    class Meta:
        model = Product
        exclude = ['is_active']
        #read_only_fields = ['supplier']
