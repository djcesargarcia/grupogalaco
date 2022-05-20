from django.db import models
from rest_framework import serializers
from order.models import Order
from article.models import Article

# Create your models here.

class OrderSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=100)
    code_buy = serializers.IntegerField()
    cuantity = serializers.IntegerField()
    date_buy = serializers.DateField(auto_now=True)
    date_out = serializers.DateField(auto_now=True)
    order_article = serializers.PrimaryKeyRelatedField(Article, read_only=True)
    