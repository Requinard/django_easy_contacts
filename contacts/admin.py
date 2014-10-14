from django.contrib import admin

from .models import *

class ContactAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Contact",
            {
                'fields': ('name', 'address', 'email', 'telephone')
            }
        ),
        (
            "Industry",
            {
                'fields' : ('industry', 'type')
            }
        ),
    )

    list_display = ('id', 'name', 'email', 'telephone', 'address')
    list_filter = ('industry', 'type')

class IndustryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

# Register your models here.
admin.site.register(Contact, ContactAdmin)
admin.site.register(Industry, IndustryAdmin)
admin.site.register(Type, TypeAdmin)