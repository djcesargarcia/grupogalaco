from rest_framework import serializers
from driver.models import Driver
from django.contrib.auth.models import models

class DriverSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    nif = serializers.CharField(max_length=50)
    image = serializers.ImageField()
    adress = serializers.CharField(max_length=100)
    driver_routes = serializers.PrimaryKeyRelatedField(read_only=True)  

    
    