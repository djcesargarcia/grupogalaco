from unittest.util import _MAX_LENGTH
from customer.models import Customer
from django.db import models
from rest_framework import serializers


class Customer(serializers.Serializers):
    name = serializers.CharField(max_length=50)
    dni = serializers.CharField(max_length=9)
    phone_number = serializers.CharField(max_length=9)
    postal_code = serializers.CharField(max_length=5)
    adress = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=100)
    article_customer = serializers.PrimaryKeyRelatedField(read_only=True) 
    
    