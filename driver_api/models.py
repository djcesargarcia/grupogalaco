from lib2to3.pgen2 import driver
from rest_framework import serializers
from driver.models import Driver

"""" POST Create Driver """

    
class DriverSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    nif = serializers.CharField(max_length=9)
    image = serializers.ImageField()
    adress = serializers.CharField(max_length=100)
    driver_routes = serializers.RelatedField(source='routes', read_only=True)
   
    def create(self,validated_data):
        return Driver.objects.create(**validated_data)
       
    
 
   