"""Users views."""

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)
from rest_framework.exceptions import PermissionDenied
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

# Custom permissions
from sunnysouth.marketplace.permissions.users import IsSuperUser, IsAccountOwner

# Serializers
from sunnysouth.marketplace.serializers import (
    AccountVerificationSerializer,
    UserModelSerializer,
    UserSignUpSerializer,
    ProfileModelSerializer,
    MyTokenObtainPairSerializer
)

# Models
from sunnysouth.marketplace.models import User, Product


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.filter(is_active=True, is_verified=True)
    serializer_class = UserModelSerializer
    lookup_field = 'username'

    def get_permissions(self):
        if self.action in ['signup', 'login', 'verify']:
            permissions = [AllowAny]
        elif self.action in ['list']:
            permissions = [IsAuthenticated, IsSuperUser]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    @action(detail=False, methods=['post'])
    def signup(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data

        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def verify(self, request):
        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message': 'Cuenta verificada exitosamente'}

        return Response(data, status=status.HTTP_200_OK)


class MeAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        return Response(UserModelSerializer(self.get_object()).data)

    def put(self, request, format=None):
        data = self._update(request)

        return Response(data)

    def patch(self, request, format=None):
        data = self._update(request, partial=True)

        return Response(data)

    def get_object(self):
        user = self.request.user
        if user.is_active and user.is_verified:
            return self.request.user

        raise PermissionDenied(detail='Invalid user', code='invalid_user')

    def _update(self, request, partial=False):
        user = self.get_object()
        data = request.data.get('user', {})
        serializer = UserModelSerializer(user, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
