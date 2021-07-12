
# Django
from django.contrib.auth import password_validation
from django.db import transaction

# Django rest framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from sunnysouth.marketplace.models import Manufacturer, User

# Tasks
from sunnysouth.taskapp.tasks import send_confirmation_email


class ManufacturerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        exclude = ['id']
        read_only_fields = ['reputation', 'uuid', 'user']


class UserModelSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerModelSerializer()
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
        password = data['password']
        password_confirmation = data['password_confirmation']
        if password != password_confirmation:
            raise serializers.ValidationError("Passwords don't match.")
        password_validation.validate_password(password_confirmation)

        return data

    def create(self, data):
        password = data.pop('password')
        data.pop('password_confirmation')
        manufacturer_data = data.pop('manufacturer')

        user = User.objects.create(**data, is_verified=False)
        user.set_password(password)
        user.save()
        manufacturer = Manufacturer.objects.create(user=user, **manufacturer_data)
        transaction.on_commit(lambda: send_confirmation_email.delay(user_pk=user.pk))

        return manufacturer
