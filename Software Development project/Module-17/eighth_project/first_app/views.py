from django.shortcuts import render,redirect
from . forms import RegisterForm ,ChangeUserData #django er built in function register korara jno aladha kono form create korte hbena
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm ,PasswordChangeForm , SetPasswordForm
from django.contrib.auth import authenticate ,login , logout , update_session_auth_hash  #user authentic ,log in ,logout er built in function

# Create your views here.

def home(request):
    return render(request,'home.html')

def Signup(request):
    if not request.user.is_authenticated:
        if request.method =="POST":
            form=RegisterForm(request.POST)

            if form.is_valid():
                messages.success(request,'Account created succesfully')
                # messages.warning(request,'warning')
                # messages.info(request,'info')
                
                form.save()
                print(form.cleaned_data)
        else:
            form=RegisterForm()
        return render(request,'Signup.html',{'form':form})
    
    else:
        return redirect('profile')


def userlogin(request):
    # authentic user na hole login page e jabe..r na hole profile e jabe
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data =request.POST)

            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user= authenticate(username =name, password = userpass)  #yser database e ache kina ck kora
                if user is not None:
                    login(request,user)
                    return redirect('profile') #profile page e redirect korbe

        else:
            form=AuthenticationForm() 
        return render(request,'login.html',{'form': form})
    
    else:
        return redirect('profile')


def profile(request):
    if request.user.is_authenticated:
        if request.method =="POST":
            form=ChangeUserData(request.POST,instance = request.user) #authentic user holey access korte parbe tai instance diye ck kora

            if form.is_valid():
                messages.success(request,'Account updated succesfully')
                # messages.warning(request,'warning')
                # messages.info(request,'info')
                
                form.save()
                # print(form.cleaned_data)
        else:
            form=ChangeUserData(instance = request.user)
        return render(request,'profile.html',{'form':form})
    
    else:
        return redirect('signup')
    

def userlogout(request):
    logout(request)
    # messages.success(request,'Account logged out succesfully')
    return redirect('login')


def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user,data = request.POST)

            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user) #password update korbe
                return redirect('profile')
            
        else:
            form = PasswordChangeForm(user = request.user)
        return render(request,'passchange.html',{'form':form})
    
    else:
        return redirect('login')


def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user,data = request.POST)

            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user) #password update korbe
                return redirect('profile')
            
        else:
            form = SetPasswordForm(user = request.user)
        return render(request,'passchange.html',{'form':form})
    
    else:
        return redirect('login')

    

def Change_User_Data(request):
    if request.user.is_authenticated:
        if request.method =="POST":
            form=ChangeUserData(request.POST,instance = request.user) #authentic user holey access korte parbe tai instance diye ck kora

            if form.is_valid():
                messages.success(request,'Account updated succesfully')
                # messages.warning(request,'warning')
                # messages.info(request,'info')
                
                form.save()
                print(form.cleaned_data)
        else:
            form=ChangeUserData()
        return render(request,'profile.html',{'form':form})
    
    else:
        return redirect('signup')
