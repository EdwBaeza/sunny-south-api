"""Users views."""

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.parsers import JSONParser

from sunnysouth.marketplace.permissions.users import IsSuperUser, IsSuperUserOrAccountOwner

# Serializers
from sunnysouth.marketplace.serializers import (
    AccountVerificationSerializer,
    UserModelSerializer,
    UserSignUpSerializer,
    ProfileModelSerializer,
    MyTokenObtainPairSerializer
)
from sunnysouth.marketplace.serializers import ProductModelSerializer

# Models
from sunnysouth.marketplace.models import User
from sunnysouth.marketplace.models import Product

class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """User view set.

    Handle sign up, login and account verification.
    """

    queryset = User.objects.filter(is_active=True, is_verified=True)
    serializer_class = UserModelSerializer
    lookup_field = 'username'

    def get_permissions(self):
        """Assign permissions based on action."""
        if self.action in ['signup', 'login', 'verify']:
            permissions = [AllowAny]
        elif self.action in ['update', 'partial_update', 'profile', 'destroy']:
            permissions = [IsAuthenticated, IsSuperUserOrAccountOwner]
        elif self.action in ['list']:
            permissions = [IsAuthenticated, IsSuperUser]
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
        data = UserModelSerializer(user).data
        return Response(data)

    @action(detail=False, methods=['get'])
    def me(self, request, *args, **kwargs):
        return Response(UserModelSerializer(request.user).data)

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User sign up."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def verify(self, request):
        """Account verification."""
        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message': 'Cuenta verificada exitosamente'}
        return Response(data, status=status.HTTP_200_OK)


class MyTokenObtainPairView(TokenObtainPairView):
    "Custom token serializer"
    serializer_class = MyTokenObtainPairSerializer
