from django.urls import path
from .views import QRCodeGeneratorView, AttendanceRecordView

urlpatterns = [
    path('qr-code/', QRCodeGeneratorView.as_view(), name='qr-code-generator'),
    path('record/', AttendanceRecordView.as_view(), name='attendance-record'),
]