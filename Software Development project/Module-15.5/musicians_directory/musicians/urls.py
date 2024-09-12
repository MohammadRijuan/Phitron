from django.urls import path
from . import views

urlpatterns = [
    path('add_musicians/', views.add_musicians,name='add_musicians'),
    path('edit_musicians/<int:id>',views.edit_musicians,name='edit_musicians'),
    path('delete_musicians/<int:id>',views.delete_musicians,name='delete_musicians')
]
