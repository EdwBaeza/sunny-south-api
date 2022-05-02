"""Users views."""
# Django
from django.shortcuts import get_object_or_404

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)
from rest_framework.views import APIView

# Custom permissions
from sunnysouth.marketplace.permissions.users import IsSuperUser, IsAccountOwner

# Serializers
from sunnysouth.marketplace.serializers import AssetModelSerializer, AssetSerializer

# Models
import sunnysouth.marketplace.models as attachables


class AssetAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        serializer = AssetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        attachable = self._get_attachable()
        asset = serializer.save(attachable=attachable)
        return Response(AssetModelSerializer(asset).data, status=status.HTTP_201_CREATED)

    def _get_attachable(self):
        attachable_type = self.request.data["attachable_type"].capitalize()
        attachable_id = self.request.data["attachable_id"]
        attachable_class = getattr(attachables, attachable_type)

        return get_object_or_404(attachable_class, uuid=attachable_id)
