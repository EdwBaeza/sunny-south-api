#django rest_framework
from django.db.models import query
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from sunnysouth.marketplace.models import User, Manufacturer

from sunnysouth.suppliers.serializers import ManufacturerSignUpSerializer, UserModelSerializer

class ManufacturerViewSet(
    viewsets.GenericViewSet,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin
    ):
    queryset = User.objects.filter(profile__isnull=True, manufacturer__isnull=False)


    @action(detail=False, methods=['post'])
    def signup(self, request):
        serializer = ManufacturerSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        manufacturer = serializer.save()
        data = UserModelSerializer(manufacturer.user).data

        return Response(data, status=status.HTTP_201_CREATED)
