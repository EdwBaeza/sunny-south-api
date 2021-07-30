# Django
from django.conf import settings
from django.db import transaction

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Models
from sunnysouth.marketplace.models import (
    Profile,
    User,
)

# Serializers
from sunnysouth.marketplace.serializers import AddressModelSerializer
from sunnysouth.suppliers.serializers import SupplierModelSerializer

# Tasks
from sunnysouth.taskapp.tasks import send_confirmation_email

# Utilities
import jwt

# Lib
from sunnysouth.lib.validators import validate_password


class ProfileModelSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='uuid'
     )
    class Meta:
        model = Profile
        exclude = ['id']
        read_only_fields = ['reputation', 'uuid']


class UserModelSerializer(serializers.ModelSerializer):
    profile = ProfileModelSerializer()
    supplier = SupplierModelSerializer()
    class Meta:
        """Meta class."""

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

    def update(self, instance, data):
        profile_data = data.pop('profile', {})
        instance.__dict__.update(**data)
        instance.profile.__dict__.update(**profile_data)

        instance.save()
        instance.profile.save()

        return instance


class UserSignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    # Password
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    # Name
    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    phone_number = serializers.CharField(min_length=10, max_length=17)

    profile = ProfileModelSerializer()

    def validate(self, data):
        validate_password(data)

        return data

    def create(self, data):
        data.pop('password_confirmation')
        profile_data = data.pop('profile')

        user = User.objects.create_user(**data, is_verified=False)
        Profile.objects.create(user=user, **profile_data)
        transaction.on_commit(lambda: send_confirmation_email.delay(user_pk=user.pk))

        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = {
            'email': self.user.email,
            'username': self.user.username,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name
        }

        return data


class AccountVerificationSerializer(serializers.Serializer):
    token = serializers.CharField()

    def validate_token(self, data):
        """Verify token is valid."""
        try:
            payload = jwt.decode(data, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError('Verification link has expired.')
        except jwt.PyJWTError:
            raise serializers.ValidationError('Invalid token')
        if payload['type'] != 'email_confirmation':
            raise serializers.ValidationError('Invalid token')

        self.context['payload'] = payload
        return data

    def save(self):
        """Update user's verified status."""
        payload = self.context['payload']
        user = User.objects.get(username=payload['user'])
        user.is_verified = True
        user.save()
