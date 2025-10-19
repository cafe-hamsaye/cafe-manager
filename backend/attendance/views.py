from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from .permissions import IsCafeStaff
from .serializers import ScanSerializer, AttendanceSerializer
from authentication.models import User
from .models import Attendance
import datetime
import hashlib
import os

# A secret key for generating the token.
# In a real application, this should be stored securely in environment variables.
QR_CODE_SECRET_KEY = os.environ.get('QR_CODE_SECRET_KEY', 'a-super-secret-key')

def generate_qr_token():
    """
    Generates a time-based token for the QR code.
    The token is valid for 5 minutes.
    """
    now = datetime.datetime.now()
    timestamp = int(now.timestamp() / 300)  # 5-minute interval
    message = f'{QR_CODE_SECRET_KEY}-{timestamp}'
    return hashlib.sha256(message.encode()).hexdigest()

class QRCodeGeneratorView(APIView):
    """
    View to generate a QR code token for admins.
    """
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        token = generate_qr_token()
        return Response({'token': token})

class ScanView(APIView):
    """
    View for staff to scan the QR code and record attendance.
    """
    permission_classes = [IsCafeStaff]

    def post(self, request, format=None):
        serializer = ScanSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.validated_data['token']
            status_choice = serializer.validated_data['status']

            # Validate the token
            current_token = generate_qr_token()
            if token != current_token:
                # Check the previous token to handle slight time differences
                now = datetime.datetime.now()
                timestamp = int(now.timestamp() / 300) - 1
                message = f'{QR_CODE_SECRET_KEY}-{timestamp}'
                previous_token = hashlib.sha256(message.encode()).hexdigest()
                if token != previous_token:
                    return Response({'detail': 'QR code is invalid or expired.'}, status=status.HTTP_400_BAD_REQUEST)

            # Create the attendance record
            attendance = Attendance.objects.create(
                user=request.user,
                status=status_choice
            )
            attendance_serializer = AttendanceSerializer(attendance)
            return Response(attendance_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)