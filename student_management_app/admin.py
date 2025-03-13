from django.contrib import admin
from .models import *
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'email', 'image', 'mother_name', 'father_name', 'religion']
    search_fields = ['name', 'email', 'mother_name', 'father_name', 'religion']

admin.site.register(Student, StudentAdmin)
admin.site.register(Hobby)
admin.site.register(Subject)
admin.site.register(Result)

# admin.site.register(Student)