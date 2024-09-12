from django import forms
from . models import Albums

class Album_form(forms.ModelForm):
    class Meta:
        model= Albums
        fields='__all__'