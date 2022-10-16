# Django REST Framework
from rest_framework.permissions import BasePermission


class IsAccountOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser
