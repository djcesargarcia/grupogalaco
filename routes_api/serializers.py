from rest_framework import serializers
from routes.models import Routes
from django.contrib.auth.models import models

class RoutesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    place = serializers.CharField(max_length=50)
    origin = serializers.CharField(max_length=50)
    destiny = serializers.CharField(max_length=50)
    postal_code = serializers.CharField(max_length=50)
    image = serializers.ImageField()
    
    def create(self,validated_data):
        return Routes.objects.create(**validated_data)
    
    
    