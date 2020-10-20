from django.contrib import admin
from Third_app.models import *
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Student,StudentAdmin)
