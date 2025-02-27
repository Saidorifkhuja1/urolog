from django.contrib import admin
from .models import *

@admin.register(Shifokor)
class ShifokorAdmin(admin.ModelAdmin):
    list_display = ['name']
    exclude = ['groups', 'user_permissions', 'last_login']



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']



