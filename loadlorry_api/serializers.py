from rest_framework import serializers
from loadlorry.models import LoadLorry
from django.contrib.auth.models import models

class LoadLorrySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    weight = serializers.FloatField()
    volume = serializers.FloatField()
    mma = serializers.FloatField()
    tare = serializers.FloatField()
    cuantity = serializers.FloatField()
    empty_weight = serializers.FloatField()
    total_weight = serializers.FloatField()
    
    def create(self,validated_data):
        return LoadLorry.objects.create(**validated_data)

    
    