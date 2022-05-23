from rest_framework import serializers
from article.models import Article
from provider.models import Provider
from django.contrib.auth.models import models

class ProviderSerializer(serializers.Serializer):
    
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)
    dni = serializers.CharField(max_length=9)
    phone_number = serializers.CharField(max_length=9)
    image = serializers.ImageField()
    article_provider = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Article.objects.all(),source='articles') 
    
    def create(self,validated_data):
        return Provider.objects.create(**validated_data)
    
    