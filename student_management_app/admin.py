from django.contrib import admin
from .models import Student
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['prime_id', 'name', 'email', 'image', 'mother_name', 'father_name', 'religion']
    search_fields = ['name', 'email', 'mother_name', 'father_name', 'religion']

admin.site.register(Student, StudentAdmin)

# admin.site.register(Student)