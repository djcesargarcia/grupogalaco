from django import forms
from .models import Routes

class RoutesForm(forms.ModelForm):
    class Meta:
        model = Routes
        fields = '__all__'