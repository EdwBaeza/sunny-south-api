# Django REST Framework
from random import choices
from rest_framework import serializers

# Models
from sunnysouth.marketplace.models import Asset


class AssetModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'
        read_only_fields = ['attachable_object_id', 'attachable_content_type']


class AssetSerializer(serializers.Serializer):
    ATTACHABLE_TYPES = ('user', 'profile')
    type = serializers.CharField(required=True)
    file = serializers.FileField(required=True)
    attachable_id =  serializers.CharField(required=True)
    attachable_type =  serializers.ChoiceField(choices=ATTACHABLE_TYPES, required=True)

    def create(self, data):
        return Asset.objects.create(
            image=data['file'],
            type=data['type'],
            attachable=data['attachable']
        )

