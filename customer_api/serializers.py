from unittest.util import _MAX_LENGTH
from customer.models import Customer
from django.db import models
from rest_framework import serializers
from article.models import Article


class CustomerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    dni = serializers.CharField(max_length=9)
    phone_number = serializers.CharField(max_length=9)
    postal_code = serializers.CharField(max_length=5)
    adress = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=100)
    article_customer = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Article.objects.all(), source='articles') 
    
    def create(self,validated_data):
        return Customer.objects.create(**validated_data)
    
    