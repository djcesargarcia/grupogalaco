from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from zone.models import Zone
from django.contrib.auth.models import models

class ZoneSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    postal_code = serializers.CharField(max_length=5)
    image = serializers.ImageField()
    city = serializers.CharField(max_length=50)
    population = serializers.CharField(max_length=50)
    
    def create(self,validated_data):
        return Zone.objects.create(**validated_data)
    
    
    