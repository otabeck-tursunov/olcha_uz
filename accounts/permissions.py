from rest_framework.permissions import BasePermission


class IsRegularAccount(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.role == 'Regular':
            return True
        return False


class IsAdminAccount(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.role == 'Admin':
            return True
        return False


