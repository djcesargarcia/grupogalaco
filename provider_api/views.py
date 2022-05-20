from provider.models import Provider
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ProviderSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows providers to be viewed or edited
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    permission_classes = [permissions.IsAuthenticated]




