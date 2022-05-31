from django import forms
from .models import LoadLorry

class LoadLorryForm(forms.ModelForm):
    class Meta:
        model = LoadLorry
        fields = '__all__'