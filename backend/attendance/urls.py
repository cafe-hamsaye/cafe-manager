from django.urls import path
from .views import QRCodeGeneratorView

urlpatterns = [
    path('qr-code/', QRCodeGeneratorView.as_view(), name='qr-code-generator'),
]
