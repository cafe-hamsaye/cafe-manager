from rest_framework.permissions import BasePermission
from .models import Staff

class IsStaffMember(BasePermission):
    """
    Allows access only to authenticated staff members.
    """

    def has_permission(self, request, view):
        return isinstance(request.user, Staff)
