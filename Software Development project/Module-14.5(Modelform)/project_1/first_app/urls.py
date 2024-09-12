from django.urls import path,include
from . import views
urlpatterns = [
   
    path('model/',views.model,name='client_form'),
]