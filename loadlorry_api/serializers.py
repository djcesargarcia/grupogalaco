from tabnanny import verbose
from rest_framework import serializers
from driver.models import Driver
from loadlorry.models import LoadLorry
from django.contrib.auth.models import models

class LoadLorrySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, verbose_name="id")
    weight = serializers.FloatField(verbose_name="Weight")
    volume = serializers.FloatField(verbose_name="Volume")
    mma = serializers.FloatField(verbose_name="MMA")
    tare = serializers.FloatField(verbose_name="Tare")
    cuantity = serializers.FloatField(verbose_name="cuantity")
    empty_weight = serializers.FloatField(verbose_name="Empty Weight")
    total_weight = serializers.FloatField(verbose_name="Total Weight")
    
    def create(self,validated_data):
        return LoadLorry.objects.create(**validated_data)

    
    