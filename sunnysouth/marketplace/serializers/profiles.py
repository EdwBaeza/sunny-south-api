"""Users Profile serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from sunnysouth.marketplace.models import Profile


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
