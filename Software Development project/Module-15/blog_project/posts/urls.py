from django.urls import path,include
from . import views
urlpatterns = [
    
    path('add_posts/',views.add_posts,name='add_posts'),
    path('edit_posts/<int:id>',views.edit_posts,name='edit_posts'),
    path('delete_posts/<int:id>',views.delete_posts,name='delete_posts')
]