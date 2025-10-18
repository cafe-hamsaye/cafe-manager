from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RegisterView, 
    MyTokenObtainPairView, 
    GetMeView, 
    AdminTokenObtainPairView,
    UserViewSet
)
from rest_framework_simplejwt.views import TokenRefreshView

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('admin/login/', AdminTokenObtainPairView.as_view(), name='admin_login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', GetMeView.as_view(), name='get_me'),
    path('', include(router.urls)), # Add the router's URLs to our urlpatterns
]