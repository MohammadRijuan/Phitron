from rest_framework.routers import DefaultRouter
from django.urls import path , include
from . views import PatientViewset

router= DefaultRouter() # amader router

router.register('list/',PatientViewset) # amader antenna

urlpatterns = [
    path('', include(router.urls)),
]
