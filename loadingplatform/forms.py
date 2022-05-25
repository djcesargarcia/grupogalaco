from dataclasses import fields
from django import forms
from .models import LoadingPlatform

class LoadingPlatformForm(forms.ModelForm):
    class Meta:
        model = LoadingPlatform
        fields = '__all__'