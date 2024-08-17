from django.contrib import admin
from .models import Post, CustomUser

#post admin
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'price', 'category', 'stock', 'image', 'author']

#custome user admin
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_disabled']

admin.site.register(Post, PostAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
    