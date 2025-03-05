from rest_framework import serializers
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True, default="not answered")

    class Meta:
        model = Message
        fields = ['uid', 'title', 'body', 'uploaded_at', 'status']
        read_only_fields = ['uid']


class MessageUpdateSerializer(serializers.ModelSerializer):


    class Meta:
        model = Message
        fields = ['title', 'body', 'answer', 'status']
        read_only_fields = ['status']
