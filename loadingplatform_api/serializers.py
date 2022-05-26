from rest_framework import serializers
from loadingplatform.models import LoadingPlatform
from django.contrib.auth.models import models

class LoadingPlatformSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    position = serializers.IntegerField()
    image = serializers.ImageField()
    
    def create(self,validated_data):
        return LoadingPlatform.objects.create(**validated_data)

    
    