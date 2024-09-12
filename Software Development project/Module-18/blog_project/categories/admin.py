from django.contrib import admin
from . import models
# Register your models here.

# category filtering .category wise post dekbo r seta holo slug ja automatically kore dibe
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    list_display = ['name','slug']


admin.site.register(models.Category,CategoryAdmin)