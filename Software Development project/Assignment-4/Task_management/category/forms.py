from django import forms 

from . models import TaskCategory

class Category_form(forms.ModelForm):
    class Meta:
        model = TaskCategory
        fields = '__all__'