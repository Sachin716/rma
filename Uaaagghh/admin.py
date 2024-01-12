from django.contrib import admin
from .models import *

class ServiceID(admin.ModelAdmin):
    readonly_fields = ("id",)

admin.site.register(services , ServiceID)
admin.site.register(Bookins , ServiceID)
admin.site.register(services_cateogaries)
admin.site.register(Appointment)
admin.site.register(review)
admin.site.register(IP)
admin.site.register(gall)
# Register your models here.
