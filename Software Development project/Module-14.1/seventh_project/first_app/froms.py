from django import forms

from first_app.models import StudentModel

# models form
class StudentForm(forms.ModelForm):
    # meta class use class modify korte
    class Meta:
        model = StudentModel
        fields = '__all__'
        # fields= ['name','roll']
        # exclude = ['address']
        labels ={
            'name' : 'Student Name',
            'roll' : 'Student Roll',
            'father_name' : 'Student Father Name',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': ''}),
           
        }
        help_texts = {
            'name' : "write your full name"
        }
        error_messages = {
            'name' : {"required" : "your name must be needed"}
        }

