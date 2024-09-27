from django.contrib import admin
from .models import Appointment
# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    list_display=['Patient_name','Doctor_name','appointment_status','appointment_types','symptom','time','cancel']

    def Patient_name(self, obj):
        return obj.patient.user.first_name
    
    def Doctor_name(self, obj):
        return obj.doctor.user.first_name
    
admin.site.register(Appointment,AppointmentAdmin)