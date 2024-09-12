from django.shortcuts import render,redirect

# Create your views here.
def add_profile(request):
    return render(request,'add_profile.html')

from django.contrib.auth.forms import AuthenticationForm ,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import forms


def register(request):
    if request.method == 'POST':
        reg_form = forms.RegForm(request.POST) # forms.py er for ke assign korlam

        if reg_form.is_valid(): #form ta valid kina
            reg_form.save() #jodi valid hoy tahole data save korbo
            messages.success(request,'Account has been created successfully') # data entry er por confirmation msg throw korbo
            return redirect('register') # register page ey redirect thakbe
    else:
        reg_form = forms.RegForm()  #onno thai regform e show korbe
    return render(request,'register.html',{'form':reg_form,'type': 'Register'})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST) #django built-in AuthenticationForm ke call korbo

        if form.is_valid(): #form ta valid kina
            user_name=form.cleaned_data['username'] #username r password pass korbo
            user_pass=form.cleaned_data['password']

            user=authenticate(username=user_name,password=user_pass) #user ta authentic kina r data actual kina

            if user is not None:
                messages.success(request,'logged in successful')  #jodi info correct hoy
                login(request,user) #login korabo
                return redirect('profile') #profile e niye jabo
            else:
                messages.success(request,'Your info is incorect') #r an hole dukte dibona..register korte bolbo
                return redirect('register')
    else:
        form = AuthenticationForm(request,request.POST)
    return render(request,'register.html',{'form':form,'type':'Login'}) #type dile jeta j form  seta sey akare asign korbe


def user_logout(request):
    logout(request)
    return redirect('login')