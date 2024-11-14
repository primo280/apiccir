from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class CustomUserAdmin(BaseUserAdmin):
    list_display = ('nom', 'prenom', 'email','npi','code_postal',  'telephone', 'password')
    list_filter = ('email',)
    fieldsets = (
        (None, {'fields': ('telephone', 'email')}),
        
        ('Permissions', {'fields': ('is_superuser',)}),
    )
   
    search_fields = ('email', 'password')
    ordering = ('telephone',)
    filter_horizontal = ()

admin.site.register(CustomUser, CustomUserAdmin)

