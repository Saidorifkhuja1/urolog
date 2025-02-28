from rest_framework import serializers
from .models import *

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['uid', 'title', 'body', 'uploaded_at']
        read_only_fields = ['uid']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['uid', 'message', 'title', 'body', 'uploaded_at']
        read_only_fields = ['uid']
