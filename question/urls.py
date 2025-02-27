from django.urls import path
from .views import *

urlpatterns = [
    path('api/question/', MessageListView.as_view()),
    path('api/question/create/', MessageCreateView.as_view()),
    path('api/question/<uuid:uid>/', MessageRetrieveView.as_view()),


    path('api/answers/', AnswerListView.as_view(), name='answer-list'),
    path('api/answers/create/', AnswerCreateView.as_view(), name='answer-create'),
    path('api/answers/<uuid:uid>/', AnswerRetrieveView.as_view(), name='answer-detail'),
    path('api/answers/<uuid:uid>/update/', AnswerUpdateView.as_view(), name='answer-update'),
    path('api/answers/<uuid:uid>/delete/', AnswerDeleteView.as_view(), name='answer-delete'),




]
