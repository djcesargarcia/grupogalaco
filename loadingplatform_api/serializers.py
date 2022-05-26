from rest_framework import serializers
from driver.models import Driver
from routes.models import Routes
from django.contrib.auth.models import models

class DriverSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    position = serializers.IntegerField()
    image = serializers.ImageField()
    
    def create(self,validated_data):
        return Driver.objects.create(**validated_data)

    
    