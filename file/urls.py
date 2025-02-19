from django.urls import path
from .views import search_and_upload

urlpatterns = [
    path("upload/", search_and_upload, name="search_and_upload"),
]

