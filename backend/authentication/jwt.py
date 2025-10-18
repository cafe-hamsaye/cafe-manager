from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from .models import User, Admin

class MultiModelJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        try:
            user_id = validated_token['user_id']
        except KeyError:
            raise InvalidToken('Token contained no recognizable user identification')

        # First, try to get the user from the Admin model
        try:
            return Admin.objects.get(id=user_id)
        except Admin.DoesNotExist:
            pass

        # If not an admin, try to get the user from the User model
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise InvalidToken('User not found')
