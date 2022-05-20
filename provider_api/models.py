from lib2to3.pgen2 import provider
from rest_framework import serializers
from provider.models import Provider


# Create your models here.

class Provider(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)
    dni = serializers.CharField(max_length=9)
    phone_number = serializers.CharField(max_length=9)
    image = serializers.ImageField()
    article_provider = serializers.RelatedField(source='articles', read_only=True)

def create(self,validated_data):
        return Provider.objects.create(**validated_data)