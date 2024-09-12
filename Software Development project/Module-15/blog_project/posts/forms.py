from django import forms
from . models import posts

class post_form(forms.ModelForm):
    class Meta:
        model = posts
        fields ='__all__'
        