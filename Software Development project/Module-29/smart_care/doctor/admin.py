from django.contrib import admin
from . models import Doctor,AvailableTime,Designation,Specialization,Review
# Register your models here.



admin.site.register(Doctor)
admin.site.register(AvailableTime)

class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',),}

admin.site.register(Designation)

class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}


admin.site.register(Specialization,SpecializationAdmin)
admin.site.register(Review)