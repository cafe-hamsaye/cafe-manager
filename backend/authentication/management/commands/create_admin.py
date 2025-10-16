import os
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from authentication.models import Admin

class Command(BaseCommand):
    help = 'Create a default admin user from .env variables'

    def handle(self, *args, **options):
        username = os.getenv('ADMIN_USERNAME')
        password = os.getenv('ADMIN_PASSWORD')

        if not username or not password:
            self.stdout.write(self.style.ERROR('ADMIN_USERNAME and ADMIN_PASSWORD must be set in .env file'))
            return

        if Admin.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f'Admin user "{username}" already exists.'))
            return

        hashed_password = make_password(password)
        Admin.objects.create(username=username, password=hashed_password)
        self.stdout.write(self.style.SUCCESS(f'Successfully created admin user "{username}".'))
