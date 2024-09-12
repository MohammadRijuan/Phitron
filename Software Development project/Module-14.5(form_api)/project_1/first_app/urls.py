from django.urls import path,include

from . import views

urlpatterns = [
    
    path('', views.home,name='homepage'),
    path('student_form/', views.student_form,name='student_form'),
]