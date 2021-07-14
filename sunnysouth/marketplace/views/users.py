"""Users views."""

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)
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
from sunnysouth.marketplace.models import User
from sunnysouth.marketplace.models import Product

class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.filter(is_active=True, is_verified=True)
    serializer_class = UserModelSerializer
    lookup_field = 'username'

    def get_permissions(self):
        if self.action in ['signup', 'login', 'verify']:
            permissions = [AllowAny]
        elif self.action in ['update', 'partial_update', 'profile', 'destroy']:
            permissions = [IsAuthenticated, IsAccountOwner]
        elif self.action in ['list']:
            permissions = [IsAuthenticated, IsSuperUser, IsAccountOwner]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    @action(detail=True, methods=['put', 'patch'])
    def profile(self, request, *args, **kwargs):
        """Update profile data."""
        user = self.get_object()
        partial = request.method == 'PATCH'
        serializer = ProfileModelSerializer(
            user.profile,
            data=request.data,
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(UserModelSerializer(user).data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def me(self, request, *args, **kwargs):
        return Response(UserModelSerializer(request.user).data, status=status.HTTP_200_OK)

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


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
