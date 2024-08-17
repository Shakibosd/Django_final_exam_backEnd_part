from django.contrib import admin
from .models import CustomUser

#custome user admin
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_disabled']

admin.site.register(CustomUser, CustomUserAdmin)
    