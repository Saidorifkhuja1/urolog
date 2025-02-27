from django.urls import path
from .views import (
    NewsCreateView, NewsRetrieveView, NewsUpdateView,
    NewsDeleteView, NewsListView
)

urlpatterns = [
    path('news_list/', NewsListView.as_view()),
    path('news/create/', NewsCreateView.as_view()),
    path('news_detail/<uuid:uid>/', NewsRetrieveView.as_view()),
    path('update_news/<uuid:uid>/', NewsUpdateView.as_view()),
    path('delete_news/<uuid:uid>/', NewsDeleteView.as_view()),
]