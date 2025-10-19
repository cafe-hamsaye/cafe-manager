from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
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