from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class StaffManager(BaseUserManager):
    def create_user(self, number, password=None, **extra_fields):
        if not number:
            raise ValueError('The Number field must be set')
        user = self.model(number=number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, number, password=None, **extra_fields):
        # Superusers for this model are not intended, but the method is required.
        extra_fields.setdefault('is_staff_member', True) # Custom field, not Django's is_staff
        extra_fields.setdefault('is_superuser', False)
        return self.create_user(number, password, **extra_fields)

class Staff(AbstractBaseUser):
    number = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    # We add a custom is_staff_member to avoid conflicts with Django's own is_staff
    is_staff_member = models.BooleanField(default=True)

    objects = StaffManager()

    USERNAME_FIELD = 'number'

    def __str__(self):
        return self.number

    # These methods are required for Django admin integration, even if not used.
    def has_perm(self, perm, obj=None):
        return self.is_staff_member

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        # Required by Django admin.
        return self.is_staff_member