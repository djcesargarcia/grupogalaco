from rest_framework import serializers
from vehicle.models import Vehicle
from django.contrib.auth.models import models

class VehicleSerializer(serializers.Serializer):
    
    id = serializers.IntegerField(read_only=True)
    brand = serializers.CharField(max_length=50)
    model = serializers.CharField(max_length=50)
    plate = serializers.CharField(max_length=9)
    wheels = serializers.IntegerField()
    image = serializers.ImageField()
    
    def create(self,validated_data):
        return Vehicle.objects.create(**validated_data)
    
    