from rest_framework import serializers
from .models import Attendance

class AttendanceRecordSerializer(serializers.Serializer):
    token = serializers.CharField()
    status = serializers.ChoiceField(choices=[('in', 'Clock In'), ('out', 'Clock Out')])

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
