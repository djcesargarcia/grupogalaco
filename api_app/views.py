from lib2to3.pgen2.driver import Driver
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from api_app.serializers import DrivertItemSerializer
from .models import DriverItem 
from .permissions import IsOwnerOrReadOnly

class DriverItemViews(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        if request.method == 'GET':
            snippets = DriverItem.objects.all()
        serializer = DrivertItemSerializer(snippets, many=True)
        return Response(serializer.data)