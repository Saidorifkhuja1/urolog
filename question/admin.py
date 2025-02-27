from django.contrib import admin
from .models import *

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['title']

