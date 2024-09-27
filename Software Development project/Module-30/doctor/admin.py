from django.contrib import admin
from . models import Doctor,AvailableTime,Designation,Specialization,Review

# Register your models here.
admin.site.register(Doctor)
admin.site.register(AvailableTime)

class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    list_display = ['name', 'slug']
    
class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    list_display = ['name', 'slug']
    
admin.site.register(Designation, DesignationAdmin)
admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(Review)