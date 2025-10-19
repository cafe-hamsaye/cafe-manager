from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission

class StaffManager(BaseUserManager):
    def create_user(self, number, password=None, **extra_fields):
        if not number:
            raise ValueError('The Number must be set')
        user = self.model(number=number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, number, password=None, **extra_fields):
        # No superuser concept for this model, but method is required
        extra_fields.setdefault('is_staff_member', True)
        extra_fields.setdefault('is_superuser', False)
        return self.create_user(number, password, **extra_fields)

class Staff(AbstractBaseUser, PermissionsMixin):
    number = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff_member = models.BooleanField(default=True) # To identify them, separate from Django's is_staff

    objects = StaffManager()

    USERNAME_FIELD = 'number'

    # Add related_name to avoid clashes with other user models
    groups = models.ManyToManyField(Group, related_name='staff_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='staff_permissions', blank=True)

    def __str__(self):
        return self.number

    # Django admin requires this property
    @property
    def is_staff(self):
        return self.is_staff_member

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True
