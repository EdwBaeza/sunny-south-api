"""Products permissions."""

#Django REST framework
from rest_framework.permissions import BasePermission

class IsValidCurrentUser(BasePermission):
    """ Allow access only to users are active and verified"""

    def has_permission(self, request, view):
        username = view.kwargs['username']
        return request.user.is_superuser or request.user.username == username

