"""User permissions."""

# Django REST Framework
from rest_framework.permissions import BasePermission


class IsAccountOwner(BasePermission):
    """Allow access only to objects owned by the requesting user."""

    def has_object_permission(self, request, view, obj):
        """Check obj and user are the same."""
        return request.user == obj


class IsSuperUser(BasePermission):

    def has_permission(self, request, view):
        """Allow access only if user is superuser."""
        return request.user.is_superuser


class IsSuperUserOrAccountOwner(BasePermission):

    def has_permission(self, request, view):
        """Allow access only if user is superuser."""
        obj = view.get_object()
        return self.has_object_permission(request, view, obj)

    def has_object_permission(self, request, view, obj):
        """Check obj and user are the same."""
        return request.user == obj or request.user.is_superuser
