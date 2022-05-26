from zone.models import Zone
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ZoneSerializer

# Create your views here.

class ZoneViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited
    """
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    permission_classes = [permissions.IsAuthenticated]
    

