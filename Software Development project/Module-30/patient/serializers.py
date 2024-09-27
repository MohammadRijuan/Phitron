from rest_framework import serializers
from . models import Patient

# ei model obj ke json e convert korbo
class PatientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False) # ata dile random user number ta thakbena
    class Meta:
        model = Patient
        fields = '__all__'