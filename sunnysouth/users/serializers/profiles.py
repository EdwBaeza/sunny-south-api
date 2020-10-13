"""Users Profile serializers."""

# Django
from django.core.validators import RegexValidator

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# Models
from sunnysouth.users.models import Profile

class ProfileModelSerializer(serializers.ModelSerializer):
    """User model serializer."""
    user = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='uuid'
     )

    class Meta:
        """Meta class."""

        model = Profile
        exclude = ['id']
        read_only_fields = ['reputation', 'uuid', 'is_client', 'is_supplier']
