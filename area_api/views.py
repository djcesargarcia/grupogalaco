from area.models import Area
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import AreaSerializer


class AreaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows drivers to be viewed or edited.
    """
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    permission_classes = [permissions.IsAuthenticated]
