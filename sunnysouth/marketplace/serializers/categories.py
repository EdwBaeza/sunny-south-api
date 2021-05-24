""" Serializers Product Category."""

#django
from rest_framework import serializers

#models
from sunnysouth.marketplace.models import Category


class CategoryModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['uuid']
