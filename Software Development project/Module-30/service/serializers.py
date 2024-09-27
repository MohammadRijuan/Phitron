from rest_framework import serializers
from . models import Service

# ei model obj ke json e convert korbo
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'