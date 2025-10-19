from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Staff

class StaffJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        try:
            user_id = validated_token['user_id']
            # We add a specific claim to staff tokens to identify them
            if 'is_staff_member' in validated_token:
                return Staff.objects.get(id=user_id)
        except (KeyError, Staff.DoesNotExist):
            return None
        return None
