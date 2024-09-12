from django.urls import path,include
from . import views
urlpatterns = [
    
    path('add_albums/', views.add_albums,name='add_albums'),
    
]