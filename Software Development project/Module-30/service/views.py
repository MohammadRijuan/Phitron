from django.shortcuts import render
from rest_framework import viewsets


from . models import Service
from . serializers import ServiceSerializer
# Create your views here.

# model er data json e convert hoye jabe
class ServiceViewset(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

