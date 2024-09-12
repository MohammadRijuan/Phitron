from django import forms
from . models import category

class Category_form(forms.ModelForm):
    class Meta:
        model = category
        fields ='__all__'
        