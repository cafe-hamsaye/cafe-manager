from rest_framework_simplejwt.authentication import JWTAuthentication
from authentication.models import Admin, User
from staff.models import Staff

class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        try:
            user_id = validated_token['user_id']

            # Check for custom claims to identify the user type
            if 'is_admin' in validated_token:
                return Admin.objects.get(id=user_id)
            elif 'is_staff_member' in validated_token:
                return Staff.objects.get(id=user_id)
            else:
                # Default to the regular User model
                return User.objects.get(id=user_id)

        except (KeyError, Admin.DoesNotExist, Staff.DoesNotExist, User.DoesNotExist):
            return None