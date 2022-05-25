from rest_framework import serializers
from area.models import Area
from django.contrib.auth.models import models

class AreaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    postal_code = serializers.CharField(max_length=50)
    image = serializers.ImageField()
    municipality = serializers.CharField(max_length=50)
     
    
    def create(self,validated_data):
        return Area.objects.create(**validated_data)
