from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import FormView
from . forms import RegForm,UserUpdateForm
from django.contrib.auth import login,logout
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import  reverse_lazy
from django.views import View

# Create your views here.

class UserRegistrationView(FormView):
    template_name= 'accounts/user_registration.html'
    form_class = RegForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return super().form_valid(form) #formvalid call hobe jodi  form valid hoy


class UserLoginView(LoginView):
    template_name='accounts/user_login.html'
    
    def get_success_url(self):
        return reverse_lazy ('home')
    
class UserLogoutView(LogoutView):
    def get_success_url(self):

        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')


class UserBankAccountUpdateView(View):
    template_name = 'accounts/profile.html'
    
    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})


from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from transactions.views import send_transaction_email
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.decorators import login_required


def send_transaction_email2(user, subject, template):
    message = render_to_string(template, {
        'user': user,
    })
    email = EmailMultiAlternatives(subject, '', to=[user.email])
    email.attach_alternative(message, "text/html")
    
    email.send()
    

@login_required
def password_change(request):
    form = PasswordChangeForm(user=request.user)
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            send_transaction_email2(request.user, "Password Change Message","accounts/password_email.html",)
            return redirect("profile")
    
    
    return render(request, 'accounts/password_change.html', {"form": form})