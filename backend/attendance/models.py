from django.db import models
from authentication.models import User

class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('in', 'Clock In'), ('out', 'Clock Out')])

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.status} at {self.timestamp}'