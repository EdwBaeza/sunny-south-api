""" Products serializers."""

#django
from django.conf import settings
from django.contrib.auth import authenticate

#rest_framework
from rest_framework import serializers

# #serializers

# from sunnysouth.sales.serializers import ProductCategoryModelSerializer

#models
from sunnysouth.sales.models import Product


class ProductModelSerializer(serializers.ModelSerializer):
    """ Product Model Serializer Create, Update and Delete """
    #product_category = serializers.StringRelatedField()
    #product_category = serializers.SlugRelatedField(slug_field='name')
    
    #picture = serializers.ImageField(required=None)
    class Meta:
        model = Product
        exclude = ['is_active']
        #read_only_fields = ['supplier']

class ProductListSerializer(serializers.ModelSerializer):
    """ Product Serializer when the request is list """
    product_category = serializers.StringRelatedField()
    class Meta:
        model = Product
        exclude = ['is_active']