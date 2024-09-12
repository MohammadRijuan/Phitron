from django import forms 

from . models import TaskModel

class Task_form(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'