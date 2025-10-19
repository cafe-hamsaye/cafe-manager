from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Staff
from .serializers import StaffSerializer, StaffTokenObtainPairSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all().order_by('-id')
    serializer_class = StaffSerializer
    permission_classes = [permissions.IsAdminUser]

# This now mirrors MyTokenObtainPairView exactly
class StaffTokenObtainPairView(TokenObtainPairView):
    serializer_class = StaffTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            response.data['message'] = 'ورود با موفقیت انجام شد'
        return response

class GetMeView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = StaffSerializer

    def get_object(self):
        return self.request.user
