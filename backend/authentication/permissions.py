import jwt
from django.conf import settings
from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """
    Custom permission to only allow users with 'is_admin' claim.
    This method manually decodes the token to ensure reliability.
    """
    def has_permission(self, request, view):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return False

        try:
            # Get the token from the header
            token = auth_header.split(' ')[1]
            
            # Decode the token without verification to inspect its payload.
            # Verification is already handled by the authentication backend.
            # We just need to check our custom claim.
            payload = jwt.decode(token, options={"verify_signature": False})
            
            # Check if the 'is_admin' claim is present and true
            return payload.get('is_admin') == True
            
        except (jwt.exceptions.DecodeError, IndexError):
            # If token is malformed or header is incorrect
            return False