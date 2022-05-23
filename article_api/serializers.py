from django.db import models
from rest_framework import serializers

# Create your models here.

class ArticleSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    weigth = serializers.CharField(max_length=5)
    image = serializers.ImageField()
    price = serializers.DecimalField(max_digits=4, decimal_places=2)