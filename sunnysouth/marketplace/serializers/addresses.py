# Django REST Framework
from rest_framework import serializers

# Models
from sunnysouth.marketplace.models import Address


class AddressModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        read_only_fields = ['addressable_object_id', 'addressable_content_type']
