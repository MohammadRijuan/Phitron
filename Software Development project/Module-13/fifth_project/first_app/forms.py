#  we wil code in python and it will turn into a html 
# we r using form api

from django import forms
from django.core import validators

class contactForm(forms.Form):
    # form field-

    # name= forms.CharField(label='User Name')
    # email= forms.EmailField(label='User Email')
    # age= forms.IntegerField()
    # weight= forms.FloatField()
    # balance= forms.DecimalField()
    # check= forms.BooleanField()
    # birthday= forms.DateField()
    # appointment= forms.DateTimeField()
    # CHOICES= [('S','Small'),('M','Medium'),('L','Large')]
    # size= forms.ChoiceField(choices=CHOICES)
    # meal= [('P','Pepparoni'),('M','Mushroom'),('B','Beef')]
    # pizza= forms.MultipleChoiceField(choices=meal)


    # how to upload a file-

    # name= forms.CharField(label='User Name')
    # file= forms.FileField()


    # field argument-

    # name= forms.CharField(label='Full Name : ',initial='Rijuan', help_text='Enter Your name/bla bla')
    # # to remove star mark requied will be false..then can submit blank anything 
    # text= forms.CharField(required=False)
    # # field will be there but couldnot do or write anything
    # text1= forms.CharField(required=False,disabled=True)


    
    # widgets == field to html input-
    # widgets makes our form field more reliable and beautiful
    
    text= forms.CharField(required=False,widget =forms.Textarea)
    email= forms.EmailField(label='User Email')

    age=forms.CharField(widget=forms.NumberInput())

    weight=forms.FloatField()
    balance=forms.DecimalField()
    check=forms.BooleanField()

    birthday=forms.CharField(widget=forms.DateInput(attrs={'type':'date'}))

    appointment=forms.CharField(widget=forms.DateInput(attrs={'type':'datetime-local'}))

    CHOICES=[('S','Small'),('M','Medium'),('L','Large')]
    
    size=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
    
    meal=[('P','Pepparoni'),('M','Mushroom'),('B','Beef')]
    pizza= forms.MultipleChoiceField(choices=meal,widget=forms.CheckboxSelectMultiple)


    # we can modify our html id class style bla bla
    text1= forms.CharField(required=False,widget =forms.Textarea(attrs ={'id' : 'text_area','class' : 'class1 class2','placeholder':'Enter ur text'}))

     
# class StudentData(forms.Form):
#     name =forms.CharField(widget=forms.TextInput)
#     email =forms.CharField(widget=forms.EmailInput)  
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10 :
    #         raise forms.ValidationError("Enter a name at least 12 character")
    #     return valname
    
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Your email must contain .com")
    #     return valemail


    # def clean(self):
    #     cleaned_data =super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
        
    #     if len(valname) < 10 :
    #         raise forms.ValidationError("Enter a name at least 12 character")

    
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Your email must contain .com")
        
def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError('enter a value at least 10characters')
class StudentData(forms.Form):
    name =forms.CharField(widget=forms.TextInput,validators=[validators.MaxLengthValidator(10,message="Enter a name at max 10 character")])
    name1 =forms.CharField(widget=forms.TextInput,validators=[validators.MinLengthValidator(10,message="Enter a name at least 10 character")])
    text =forms.CharField(widget=forms.TextInput,validators=[])
    email =forms.CharField(widget=forms.EmailInput,validators=[validators.EmailValidator(message='Enter a valid email')])
    age=forms.IntegerField(validators=[validators.MaxValueValidator(34,message='age must be max 34'),validators.MinValueValidator(24,message='age must be main 34')])
    file=forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'],message='file extensio must be ended with .pdf')])




    # regex,url validator


class passwordValidationProject(forms.Form):
    name= forms.CharField(widget=forms.TextInput)
    password= forms.CharField(widget=forms.PasswordInput)
    re_type_password=forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_re_pass = self.cleaned_data['re_type_password']
        val_name = self.cleaned_data['name']
        if val_re_pass != val_pass:
            raise forms.ValidationError('password does not match')
        if len(val_name) < 15:
            raise forms.ValidationError('name must be 15 characters') 