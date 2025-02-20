from django.urls import path
from .views import search_file

urlpatterns = [
    path("upload/", search_file, name="search_and_upload"),
]

