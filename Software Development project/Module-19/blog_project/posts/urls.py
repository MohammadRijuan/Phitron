from django.urls import path,include
from . import views
urlpatterns = [
    
    # path('add_posts/',views.add_posts,name='add_posts'),
    path('add_posts/',views.AddPostCreateView.as_view(),name='add_posts'),

    # path('edit_posts/<int:id>',views.edit_posts,name='edit_posts'),
    path('edit_posts/<int:id>',views.EditPostView.as_view(),name='edit_posts'),

    # path('delete_posts/<int:id>',views.delete_posts,name='delete_posts')
    path('delete_posts/<int:id>',views.DeletePostView.as_view(),name='delete_posts'),
    
    
    path('detail_post/<int:id>',views.DetailPostView.as_view(),name='detail_posts'),
]