from django import forms
from .models import Dock

class DockForm(forms.ModelForm):
    class Meta:
        model = Dock
        fields = '__all__'