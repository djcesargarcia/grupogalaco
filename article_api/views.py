from article.models import Article
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ArticleSerializers

# Create your views here.

class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    permission_classes = [permissions.IsAuthenticated]
    

