from loadingplatform.models import LoadingPlatform
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import LoadingPlatformSerializer


class DriverViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows drivers to be viewed or edited.
    """
    queryset = LoadingPlatform.objects.all()
    serializer_class = LoadingPlatformSerializer
    permission_classes = [permissions.IsAuthenticated]
