from rest_framework import serializers
from routes.models import Routes

"""" POST Create Driver """

    
class RoutesSerializer(serializers.Serializer):
    place = serializers.CharField(max_length=100)
    origin = serializers.CharField(max_length=100)
    destiny = serializers.CharField(max_length=100)
    image = serializers.ImageField()
      
    def create(self,validated_data):
        return Routes.objects.create(**validated_data)