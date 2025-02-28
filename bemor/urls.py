from django.urls import path
from .views import *

urlpatterns = [
    path('bemor_create/', BemorCreateView.as_view()),
    path('bemor_detail/<uuid:uid>/', BemorRetrieveView.as_view()),
    path('update_bemor/<uuid:uid>/', BemorUpdateView.as_view()),
    path('delete_bemor/<uuid:uid>/', BemorDeleteView.as_view()),
    path('bemor_list/', BemorListView.as_view()),
    path('bemor_download/<uuid:uid>/', BemorDocxDownloadView.as_view()),
    path('bemor_search/', BemorSearchView.as_view(),)
]




