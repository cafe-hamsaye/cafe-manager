from django.db import models
import uuid
import os

def menu_image_filename(instance, filename):
    """
    Generates a unique filename for the menu item image using UUID.
    """
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('menu_images', filename)

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to=menu_image_filename)

    def __str__(self):
        return self.name
