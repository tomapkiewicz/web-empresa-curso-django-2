from django.contrib import admin
from .models import Page


# Register your models here.
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('updated', 'created')
    list_display = ('title', 'orden')

admin.site.register(Page,PageAdmin)