from django.db import models
from staff.models import Staff

class Attendance(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='attendances')
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('in', 'Clock In'), ('out', 'Clock Out')])

    def __str__(self):
        return f'{self.staff.number} - {self.status} at {self.timestamp}'
