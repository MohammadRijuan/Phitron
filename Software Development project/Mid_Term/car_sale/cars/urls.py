from django.urls import path
from . import views
from car_sale.views import home

urlpatterns = [
    path('add_car/',views.AddCarView.as_view(),name='add_car'),
    path('car_list/',views.Car_list.as_view(),name='car_list'),
    path('category/<slug:category_slug>/',views.car_list_by_brand, name='category_wise_view'),
    path('',views.car_list_by_brand, name='car_list'),
    path('details/<int:id>', views.DetailPostView.as_view(), name='car_detail'),
    path('purchase/<int:car_id>/', views.purchased_cars, name='purchase_car'),
    
]