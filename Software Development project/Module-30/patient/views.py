from django.shortcuts import render
from rest_framework import viewsets


from . models import Patient
from . serializers import PatientSerializer
# Create your views here.

# model er data json e convert hoye jabe
class PatientViewset(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

