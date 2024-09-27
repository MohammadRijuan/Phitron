from rest_framework import serializers
from . models import ContactUs

# ei model obj ke json e convert korbo
class ContactUsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'