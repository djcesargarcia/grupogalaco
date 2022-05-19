from rest_framework import serializers
from routes.models import Routes
from django.contrib.auth.models import models

class DriverSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    nif = serializers.CharField(max_length=50)
    image = serializers.ImageField()
    adress = serializers.CharField(max_length=100)
    
    
    