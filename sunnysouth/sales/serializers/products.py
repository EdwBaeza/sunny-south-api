""" Products serializers."""
import pprint
# Django
from django.conf import settings
from django.contrib.auth import authenticate

# rest_framework
from rest_framework import serializers

# Serializers
from sunnysouth.sales.serializers.categories import CategoryModelSerializer
from sunnysouth.users.serializers import UserModelSerializer

# Models
from sunnysouth.sales.models import Product, Category
from sunnysouth.users.models.profiles import Profile


class ProductModelSerializer(serializers.ModelSerializer):
    """ Product Model Serializer Create, Update and Delete """

    supplier = serializers.SerializerMethodField()
    category = serializers.CharField(max_length=300)

    def get_supplier(self, obj):
        return obj.supplier.user.username

    class Meta:
        model = Product
        exclude = ['id', 'is_active']
        read_only_fields = ['uuid', 'supplier']

    def validate_category(self, data):
        try:
            category = Category.objects.get(uuid=data)
        except Category.DoesNotExist:
            raise serializers.ValidationError(f'No existe la categoria del producto')

        return category

    def validate_code(self, data):
        if Product.objects.filter(code=data).exists():
            raise serializers.ValidationError(f'Codigo de producto existente')

        return data

    def validate(self, data):
        data['supplier'] = self.context['supplier']

        return data


class ProductDetailSerializer(serializers.ModelSerializer):
    """ Product Model Serializer Create, Update and Delete """

    supplier = serializers.SerializerMethodField()
    category = CategoryModelSerializer()

    def get_supplier(self, obj):
        return UserModelSerializer(obj.supplier.user).data

    class Meta:
        model = Product
        exclude = ['id', 'is_active']
        read_only_fields = ['uuid', 'supplier']


class ProductListSerializer(serializers.ModelSerializer):
    """ Product Serializer when the request is list """
    category = serializers.SlugRelatedField(
         many=False,
         read_only=True,
         slug_field='name'
    )
    supplier = serializers.SlugRelatedField(
         many=False,
         read_only=True,
         slug_field='slug_name'
    )

    class Meta:
        model = Product
        exclude = ['id', 'is_active']
