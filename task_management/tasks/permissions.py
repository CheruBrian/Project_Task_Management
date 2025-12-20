from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Custom permission to allow only owners of a task to access it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
