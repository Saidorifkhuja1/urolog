from django.contrib import admin
from .models import Bemor

@admin.register(Bemor)
class BemorAdmin(admin.ModelAdmin):
    list_display = ['name']

