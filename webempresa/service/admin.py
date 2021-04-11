from django.contrib import admin
from .models import Service


# Register your models here.
class serviceAdmin(admin.ModelAdmin):
    readonly_fields = ('updated', 'created')


admin.site.register(Service, serviceAdmin)
