from django.contrib import admin
from .models import UserProfileInfo, User

# Register your models here.
class UserProfileInfoAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserProfileInfo,UserProfileInfoAdmin)
