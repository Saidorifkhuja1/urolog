from django.contrib import admin
from rest_framework.exceptions import PermissionDenied

from .models import *

@admin.register(Shifokor)
class ShifokorAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_doctor']
    exclude = ['groups', 'user_permissions', 'last_login']

    def save_model(self, request, obj, form, change):
        if form.cleaned_data.get("password"):
            obj.set_password(form.cleaned_data["password"])

        # Ensure only superusers can modify `is_doctor`
        if not request.user.is_superuser and 'is_doctor' in form.changed_data:
            raise PermissionDenied("Only superusers can change the is_doctor status.")

        super().save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        """Make is_doctor read-only for non-superusers"""
        if not request.user.is_superuser:
            return ['is_doctor']
        return []

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']



