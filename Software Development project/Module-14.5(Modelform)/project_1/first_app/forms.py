from django import forms
from . models import Client_Data
class modelForm(forms.ModelForm):
    class Meta:
        model=Client_Data
        fields='__all__'