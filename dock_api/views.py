from customer.models import Customer
from rest_framework import viewsets
from rest_framework import permissions
from dock.models import Dock
from .serializers import DockSerializer

# Create your views here.

class DockViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited
    """
    queryset = Dock.objects.all()
    serializer_class = DockSerializer
    permission_classes = [permissions.IsAuthenticated]
    

