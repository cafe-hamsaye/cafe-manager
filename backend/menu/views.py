from rest_framework import viewsets
from .models import MenuItem
from .serializers import MenuItemSerializer
from authentication.permissions import IsAdmin

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return []
        return [IsAdmin()]
