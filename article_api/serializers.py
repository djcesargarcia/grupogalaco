from rest_framework import serializers
from article.models import Article
from django.contrib.auth.models import models
# Create your models here.

class ArticleSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    weight = serializers.CharField(max_length=5)
    image = serializers.ImageField()
    price = serializers.DecimalField(max_digits=4, decimal_places=2)