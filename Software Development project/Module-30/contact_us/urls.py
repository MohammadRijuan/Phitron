from rest_framework.routers import DefaultRouter
from django.urls import path , include
from . views import ContactUsViewset

router= DefaultRouter() # amader router

router.register('',ContactUsViewset) # amader antenna

urlpatterns = [
    path('', include(router.urls)),
]
