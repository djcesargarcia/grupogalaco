from customer.models import Customer
from rest_framework import viewsets
from rest_framework import permissions
from loadlorry.models import LoadLorry
from .serializers import LoadLorrySerializer

# Create your views here.

class LoadLorryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited
    """
    queryset = LoadLorry.objects.all()
    serializer_class = LoadLorrySerializer
    permission_classes = [permissions.IsAuthenticated]
    

