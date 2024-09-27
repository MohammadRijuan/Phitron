from rest_framework.routers import DefaultRouter
from django.urls import path , include
from . views import ServiceViewset

router= DefaultRouter() # amader router

router.register('',ServiceViewset) # amader antenna

urlpatterns = [
    path('', include(router.urls)),
]
