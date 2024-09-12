from django import forms
from . models import Car ,Comment

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand','name','description','image','quantity','price']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','body']
