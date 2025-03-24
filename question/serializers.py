from rest_framework import serializers
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import *

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

class MessageListSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True, default="not answered")
    answer = serializers.CharField(read_only=True)

    class Meta:
        model = Message
        fields = ['uid', 'title', 'body', 'uploaded_at', 'status', 'answer']
        read_only_fields = ['uid', 'status', 'answer']



class CommentSerializer(serializers.ModelSerializer):
    uid = serializers.UUIDField(read_only=True)  

    class Meta:
        model = Comment
        fields = '__all__'