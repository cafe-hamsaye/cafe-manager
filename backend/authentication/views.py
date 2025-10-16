
from rest_framework import generics, permissions, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.hashers import check_password
from .serializers import UserSerializer, MyTokenObtainPairSerializer, AdminLoginSerializer
from .models import User, Admin
from .permissions import IsAdmin


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and deleting user instances.
    Accessible only by admin users.
    """
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    permission_classes = [IsAdmin] # Use the new permission class
    http_method_names = ['get', 'delete', 'head', 'options'] # Allow only list, retrieve, destroy


class AdminLoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AdminLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        try:
            admin = Admin.objects.get(username=username)
        except Admin.DoesNotExist:
            return Response({'detail': 'نام کاربری یا رمز عبور اشتباه است'}, status=status.HTTP_401_UNAUTHORIZED)

        if not check_password(password, admin.password):
            return Response({'detail': 'نام کاربری یا رمز عبور اشتباه است'}, status=status.HTTP_401_UNAUTHORIZED)

        # Generate token manually for the admin user
        refresh = RefreshToken()
        refresh['is_admin'] = True
        refresh['user_id'] = admin.id
        refresh['username'] = admin.username

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'message': 'ورود ادمین با موفقیت انجام شد'
        }, status=status.HTTP_200_OK)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        response_data = {
            'message': 'ثبت نام با موفقیت انجام شد',
            'data': serializer.data
        }
        headers = self.get_success_headers(serializer.data)
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            response.data['message'] = 'ورود با موفقیت انجام شد'
        return response

class GetMeView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user