from customer.models import Customer
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CustomerSerializer

# Create your views here.

class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]
    

