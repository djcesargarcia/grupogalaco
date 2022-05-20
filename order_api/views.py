from order.models import Order
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import OrderSerializer

# Create your views here.

class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    

