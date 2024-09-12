from django.urls import path,include
from . import views

urlpatterns = [
   
    path('',views.home,name='home'),
    path('Signup/',views.Signup,name='Signup'),
    path('login/',views.userlogin,name='login'),
    path('logout/',views.userlogout,name='logout'),
    path('pass_change/',views.pass_change,name='pass_change'),
    path('pass_change2/',views.pass_change2,name='pass_change2'),
    path('profile/',views.profile,name='profile'),

]