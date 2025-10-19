from rest_framework import viewsets, permissions
from .models import Staff
from .serializers import StaffSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all().order_by('-id')
    serializer_class = StaffSerializer
    permission_classes = [permissions.IsAdminUser]