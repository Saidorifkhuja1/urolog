from django.urls import path
from .views import *

urlpatterns = [
    path('api/question_list/', MessageListView.as_view()),
    path('api/question/create/', MessageCreateView.as_view()),
    path('api/question_detail/<uuid:uid>/', MessageRetrieveView.as_view()),
    path('messages/<uuid:uid>/update/', MessageUpdateView.as_view()),





]
