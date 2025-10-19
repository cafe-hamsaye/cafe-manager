from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StaffViewSet, StaffTokenObtainPairView, GetMeView

router = DefaultRouter()
router.register(r'staff', StaffViewSet, basename='staff')

urlpatterns = [
    path('api/staff/login/', StaffTokenObtainPairView.as_view(), name='staff_login'),
    path('api/staff/me/', GetMeView.as_view(), name='staff_me'),
    path('api/', include(router.urls)),
]
