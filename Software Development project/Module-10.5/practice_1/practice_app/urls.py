from django.urls import path
from practice_app.views import home

urlpatterns = [
    path('',home),  
]