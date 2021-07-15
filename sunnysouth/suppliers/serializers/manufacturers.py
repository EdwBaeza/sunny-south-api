
# Django
from django.db import transaction

# Django rest framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from sunnysouth.marketplace.models import Manufacturer, User, Address

# Serializers
from sunnysouth.marketplace.serializers.addresses import AddressModelSerializer

# Tasks
from sunnysouth.taskapp.tasks import send_confirmation_email

# Lib
from sunnysouth.lib.validators import validate_password


class ManufacturerModelSerializer(serializers.ModelSerializer):
    addresses = AddressModelSerializer(many=True)

    class Meta:
        model = Manufacturer
        exclude = ['id']
        read_only_fields = ['reputation', 'uuid', 'user']


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


class ManufacturerSignUpSerializer(serializers.Serializer):
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

    manufacturer = ManufacturerModelSerializer()

    def validate(self, data):
        validate_password(data)

        return data

    def create(self, data):
        password = data.pop('password')
        data.pop('password_confirmation')
        manufacturer_data = data.pop('manufacturer') or {}
        addresses_data = manufacturer_data.pop('addresses') or []

        user = User.objects.create(**data, is_verified=False)
        user.set_password(password)
        user.save()
        manufacturer = Manufacturer.objects.create(user=user, **manufacturer_data)
        for address_data in addresses_data:
            Address.objects.create(**address_data, addressable= manufacturer)

        transaction.on_commit(lambda: send_confirmation_email.delay(user_pk=user.pk))

        return manufacturer
