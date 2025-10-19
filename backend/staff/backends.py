from django.contrib.auth.backends import BaseBackend
from .models import Staff

class StaffBackend(BaseBackend):
    def authenticate(self, request, number=None, password=None, **kwargs):
        try:
            user = Staff.objects.get(number=number)
            if user.check_password(password):
                return user
        except Staff.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Staff.objects.get(pk=user_id)
        except Staff.DoesNotExist:
            return None
