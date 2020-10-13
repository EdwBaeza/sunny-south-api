""" Products serializers."""
import pprint
# Django
from django.conf import settings
from django.contrib.auth import authenticate

# rest_framework
from rest_framework import serializers

# Serializers
from sunnysouth.sales.serializers.product_category import ProductCategoryModelSerializer
from sunnysouth.users.serializers import UserModelSerializer

# Models
from sunnysouth.sales.models import Product, ProductCategory
from sunnysouth.users.models.profiles import Profile


class ProductModelSerializer(serializers.ModelSerializer):
    """ Product Model Serializer Create, Update and Delete """

    supplier = serializers.SerializerMethodField()
    product_category = serializers.CharField(max_length=300)

    def get_supplier(self, obj):
        return obj.supplier.user.username

    class Meta:
        model = Product
        exclude = ['id', 'is_active']
        read_only_fields = ['uuid', 'supplier']

    def validate_product_category(self, data):
        try:
            product_category = ProductCategory.objects.get(uuid=data)
        except ProductCategory.DoesNotExist:
            raise serializers.ValidationError(f'No existe la categoria del producto')

        return product_category

    def validate_code(self, data):
        if Product.objects.filter(code=data).exists():
            raise serializers.ValidationError(f'Codigo de producto existente')

        return data

    def validate(self, data):
        data['supplier'] = self.context['supplier']

        return data
    #def validate_supplier(self, data):

    # def create(self, data):
    #     pprint.pprint('ProductModelSerializer')
    #     pprint.pprint(data)
    #     return super(ProductModelSerializer, self).create(data)
    # #    product_category = data.pop('product_category')
    # #    data['product_category'] = product_category['id']
    # #    product = Product.objects.create(**data)
    # #    #data['product_category'] = product_category['id']
    # #    return product



class ProductDetailSerializer(serializers.ModelSerializer):
    """ Product Model Serializer Create, Update and Delete """

    supplier = serializers.SerializerMethodField()
    product_category = ProductCategoryModelSerializer()

    def get_supplier(self, obj):
        return UserModelSerializer(obj.supplier.user).data

    class Meta:
        model = Product
        exclude = ['id', 'is_active']
        read_only_fields = ['uuid', 'supplier']

class ProductListSerializer(serializers.ModelSerializer):
    """ Product Serializer when the request is list """
    product_category = serializers.SlugRelatedField(
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
