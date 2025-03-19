from django.contrib import admin
from .models import ServicesCategory, Services

@admin.register(ServicesCategory)
class ServicesCategory(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Services)
class Services(admin.ModelAdmin):
    list_display = ['title']

