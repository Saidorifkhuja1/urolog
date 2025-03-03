from django.contrib import admin
from .models import *

@admin.register(Shifokor)
class ShifokorAdmin(admin.ModelAdmin):
    list_display = ['name']
    exclude = ['groups', 'user_permissions', 'last_login']

    def save_model(self, request, obj, form, change):
        if form.cleaned_data.get("password"):
            obj.set_password(form.cleaned_data["password"])
        super().save_model(request, obj, form, change)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']



