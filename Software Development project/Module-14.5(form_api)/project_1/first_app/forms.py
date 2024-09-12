from django import forms

class StudentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput,help_text='Enter Your name')
    Class = forms.IntegerField(help_text = "Enter your class") 
    roll = forms.IntegerField(help_text = "Enter 6 digit roll number") 
    
    address = forms.CharField(widget=forms.TextInput,max_length = 30) 

    email = forms.CharField(widget=forms.EmailInput)
    
    image= forms.FileField()
    
    birth_Date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
    
    About_yourself = forms.CharField(max_length = 50,help_text='Tell me about yourself')
    
    CHOICES= [('teamwork', 'Teamwork'),
    ('leadership', 'Leadership'),
    ('time-management', 'Time-management'),]
    
    skills = forms.MultipleChoiceField(choices=CHOICES,widget=forms.CheckboxSelectMultiple)
    
    agree_to_terms = forms.BooleanField(label="I agree to the terms and conditions",required=True)
