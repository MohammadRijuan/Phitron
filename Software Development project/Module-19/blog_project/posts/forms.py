from django import forms
from . models import posts,Comment

class post_form(forms.ModelForm):
    class Meta:
        model = posts
        # fields ='__all__'
        exclude=['author']
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','body']