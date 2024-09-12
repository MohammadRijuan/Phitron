from django import forms
from . models import Musicians

class Musician_form(forms.ModelForm):
    class Meta:
        model=Musicians
        fields='__all__'