from driver.models import Driver
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import DriverSerializer


class DriverViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [permissions.IsAuthenticated]
