from routes.models import Routes
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import RoutesSerializer


class RoutesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Routes.objects.all()
    serializer_class = RoutesSerializer
    permission_classes = [permissions.IsAuthenticated]
