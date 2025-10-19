from rest_framework.permissions import BasePermission

class IsCafeStaff(BasePermission):
    """
    Allows access only to cafe staff users.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_cafe_staff
