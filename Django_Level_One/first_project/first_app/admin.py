from django.contrib import admin
from first_app.models import *


class AccessRecordAdmin(admin.ModelAdmin):
    pass
admin.site.register(AccessRecord,AccessRecordAdmin)

class TopicAdmin(admin.ModelAdmin):
    pass
admin.site.register(Topic,TopicAdmin)

class WebpageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Webpage,WebpageAdmin)
    
