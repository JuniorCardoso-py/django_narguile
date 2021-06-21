from django import forms
from .models import Narguile

class NarguileForm(forms.ModelForm):
    class Meta:
        model = Narguile
        fields = '__all__'