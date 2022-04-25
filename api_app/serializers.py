from rest_framework import serializers
from .models import DriverItem

class DrivertItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    nif = serializers.CharField(max_length=100)
    adress = serializers.CharField(max_length=100)
    
    class Meta:
        model = DriverItem
        fields = ('__all__')