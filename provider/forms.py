from dataclasses import field, fields
from django import forms
from .models import Provider

class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = '__all__'
        