from django.contrib import admin

# Register your models here.
from .models import Task

admin.site.register(Task)

# # Project name eyantraApr2020
# #AIzaSyBRnIqOuGzvnv0y9z5wB4g5HzbV3hG26pc
# from django_google_maps import widgets as map_widgets
# from django_google_maps import fields as map_fields

# class RentalAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
#     }









