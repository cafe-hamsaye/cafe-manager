from django.urls import path
from .views import QRCodeGeneratorView, ScanView

urlpatterns = [
    path('qr-code/', QRCodeGeneratorView.as_view(), name='qr-code-generator'),
    path('scan/', ScanView.as_view(), name='scan'),
]
