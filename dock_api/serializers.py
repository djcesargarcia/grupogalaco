from unittest.util import _MAX_LENGTH
from django.db import models
from rest_framework import serializers
from dock.models import Dock


class DockSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    position = serializers.CharField(max_length=50)
    image = serializers.ImageField()
    
    def create(self,validated_data):
        return Dock.objects.create(**validated_data)
    