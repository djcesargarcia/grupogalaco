from vehicle.models import Vehicle
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import VehicleSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticated]
