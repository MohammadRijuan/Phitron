from django.urls import path
from first_app import views

urlpatterns = [

    path('',views.home,name='homepage'),
    path('delete/<int:roll>',views.delete_student,name='delete_student'),
]