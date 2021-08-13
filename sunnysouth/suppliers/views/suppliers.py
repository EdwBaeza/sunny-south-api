# Django Rest Framework
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

# Models
from sunnysouth.marketplace.models import User

# Serializers
# from sunnysouth.marketplace.serializers.users import UserModelSerializer
from sunnysouth.suppliers.serializers import SupplierSignUpSerializer, SupplierModelSerializer

class SupplierViewSet(
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = User.objects.filter(profile__isnull=True, supplier__isnull=False)

    @action(detail=False, methods=['post'])
    def signup(self, request):
        serializer = SupplierSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        supplier = serializer.save()

        return Response(SupplierModelSerializer(supplier).data, status=status.HTTP_201_CREATED)
