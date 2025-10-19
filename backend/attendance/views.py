from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import AttendanceRecordSerializer, AttendanceSerializer
from .models import Attendance
import datetime
import hashlib
import os

# A secret key for generating the token.
QR_CODE_SECRET_KEY = os.environ.get('QR_CODE_SECRET_KEY', 'a-super-secret-key')

def generate_qr_token():
    now = datetime.datetime.now()
    timestamp = int(now.timestamp() / 10)  # 10-second interval
    message = f'{QR_CODE_SECRET_KEY}-{timestamp}'
    return hashlib.sha256(message.encode()).hexdigest()

class QRCodeGeneratorView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        token = generate_qr_token()
        return Response({'token': token})

from staff.permissions import IsStaffMember

class AttendanceRecordView(APIView):
    permission_classes = [IsStaffMember]

    def post(self, request, format=None):
        serializer = AttendanceRecordSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.validated_data['token']
            status_choice = serializer.validated_data['status']

            # Validate the token
            current_token = generate_qr_token()
            # Check current and previous token to avoid timing issues
            now = datetime.datetime.now()
            timestamp = int(now.timestamp() / 10) - 1
            message = f'{QR_CODE_SECRET_KEY}-{timestamp}'
            previous_token = hashlib.sha256(message.encode()).hexdigest()

            if token != current_token and token != previous_token:
                return Response({'detail': 'QR code is invalid or expired.'}, status=status.HTTP_400_BAD_REQUEST)

            # Create the attendance record
            attendance = Attendance.objects.create(
                staff=request.user,
                status=status_choice
            )
            attendance_serializer = AttendanceSerializer(attendance)
            return Response(attendance_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)