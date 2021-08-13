# Django REST Framework
from rest_framework.permissions import BasePermission


class IsAccountOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class IsSuperUserOrAccountOwner(BasePermission):
    def has_permission(self, request, view):
        obj = view.get_object()
        return self.has_object_permission(request, view, obj)

    def has_object_permission(self, request, view, obj):
        return request.user == obj or request.user.is_superuser
