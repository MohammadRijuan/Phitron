from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render,redirect
from . forms import RegForm,ChangeUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth import authenticate,update_session_auth_hash,login,logout
from django.contrib.auth.decorators import login_required
from cars.models import Car,Purchase

# Create your views here.
def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)

        if reg_form.is_valid():
            reg_form.save()
            messages.success(request,'Account has been created successfully')
            return redirect("login")
    else:
        reg_form = RegForm(request.POST)
    return render(request,'register.html',{'form':reg_form,'type':'Register'})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request,request.POST)

        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']

            user = authenticate(username=user_name,password=user_pass)

            if user is not None:
                messages.success(request,'logged in succesfully')
                login(request,user)
                return redirect ('profile')
            else:
                messages.success(request,'your info is incorrect')
                return redirect('register')
    else:
        form = AuthenticationForm(request,request.POST)
    return render(request,'register.html',{'form':form,'type':'Login'})


# we can use class based user login instead of using function here is one:
# i will use class based user login,logout in this project
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class UserLoginView(LoginView):
    template_name= 'register.html'

    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request,'logged in succesfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request,'info is incorrrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Login'
        return context



def user_logout(request):
    logout(request)
    return redirect('login')


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import RedirectView  

class UserLogoutView(LoginRequiredMixin,RedirectView):
    url = reverse_lazy('login')

    def get(self,request,*args,**kwargs):
        logout(request)
        messages.success(request,'Logged out successfully')
        return super().get(request, *args, **kwargs)


def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,data=request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Passwor Upated successfully')
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request,'pass_change.html',{'form':form})


@login_required
def profile(request):
    return render(request,'profile.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':  
        profile_form = ChangeUserForm(request.POST,instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,'Profile has been updated sucessfully')
            return redirect('profile')
    else:
        profile_form = ChangeUserForm(instance=request.user)
    return render(request,'edit_profile.html',{'form':profile_form})



@login_required
def purchase_list(request):
    purchases = Purchase.objects.all()
    return render(request, 'purchase_list.html', {'purchases': purchases})