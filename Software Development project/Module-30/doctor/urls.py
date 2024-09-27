from rest_framework.routers import DefaultRouter
from django.urls import path , include
from . views import DoctorViewset,SpecializationViewset,DesignationViewset,AvailableTimeViewset,ReviewViewset

router= DefaultRouter() # amader router

router.register('list/',DoctorViewset) # amader antenna
router.register('Specialization/',SpecializationViewset) # amader antenna
router.register('Designation/',DesignationViewset) # amader antenna
router.register('AvailableTime/',AvailableTimeViewset) # amader antenna
router.register('Review/',ReviewViewset) # amader antenna

urlpatterns = [
    path('', include(router.urls)),
]
