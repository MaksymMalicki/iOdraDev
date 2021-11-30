from django.contrib import admin
from .models import TelephoneBlock, TelephoneUnit

class TelephoneBlockAdminInline(admin.TabularInline):
    model = TelephoneUnit
    show_change_link = True
    view_on_site = False
    extra = 0

class TelephoneBlockAdmin(admin.ModelAdmin):
    inlines = [
        TelephoneBlockAdminInline
    ]

admin.site.register(TelephoneBlock, TelephoneBlockAdmin)
