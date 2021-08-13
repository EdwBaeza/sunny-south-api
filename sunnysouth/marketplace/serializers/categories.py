# Django
from rest_framework import serializers

# Models
from sunnysouth.marketplace.models import Category


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['uuid']
