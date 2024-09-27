from rest_framework import serializers
from . models import Doctor,Specialization,Designation,AvailableTime,Review

# ei model obj ke json e convert korbo
class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False) # ata dile random user number ta thakbena
    specialization = serializers.StringRelatedField(many=True) # ata dile random user number ta thakbena
    designation = serializers.StringRelatedField(many=True) # ata dile random user number ta thakbena
    available_time = serializers.StringRelatedField(many=True) # ata dile random user number ta thakbena
    class Meta:
        model = Doctor
        fields = '__all__'


class SpecializationSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Specialization
        fields = '__all__'


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'


class AvailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableTime
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'