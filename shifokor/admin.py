from django.contrib import admin
from rest_framework.exceptions import PermissionDenied

from .models import *

@admin.register(Shifokor)
class ShifokorAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'phone_number', 'email', 'is_active']
    exclude = ['groups', 'user_permissions', 'last_login']
    ordering = ['phone_number']
    list_filter = ['is_active', 'is_admin', 'is_doctor']

    # Show all fields in a single-page form
    fields = [
        'phone_number', 'password',
        'name', 'last_name', 'email', 'photo',
        'is_active', 'is_admin', 'is_doctor',
        'category', 'description'
    ]

    def save_model(self, request, obj, form, change):
        if form.cleaned_data.get("password"):
            obj.set_password(form.cleaned_data["password"])  # Ensure password hashing
        super().save_model(request, obj, form, change)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']



