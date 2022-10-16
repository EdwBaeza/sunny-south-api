
# Django
from django.db import transaction

# Django rest framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from sunnysouth.marketplace.models import Supplier, User, Address

# Serializers
from sunnysouth.marketplace.serializers.addresses import AddressModelSerializer

# Services
from sunnysouth.suppliers.services import SupplierCreateService

# Lib
from sunnysouth.lib.validators import validate_password


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            'id',
            'is_active',
            'password',
            'is_staff',
            'is_superuser',
            'is_verified',
            'groups',
            'user_permissions'
        ]
        read_only_fields = ['username', 'email', 'uuid']

class SupplierModelSerializer(serializers.ModelSerializer):
    addresses = AddressModelSerializer(many=True, required=False)
    user = UserModelSerializer(required=False)
    class Meta:
        model = Supplier
        exclude = ['id']
        read_only_fields = ['reputation', 'uuid', 'user']


class SupplierSignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    phone_number = serializers.CharField(min_length=10, max_length=17)

    supplier = SupplierModelSerializer()

    def validate(self, data):
        validate_password(data)

        return data

    def create(self, data):
        return SupplierCreateService.execute(params=data)
