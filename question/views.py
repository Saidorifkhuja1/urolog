from rest_framework import generics

from account.permissions import IsDoctorOrAdmin
from .models import Message
from .serializers import *
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response


class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        """Ensure the status is always 'not answered' when creating a new message."""
        serializer.save(status='not answered')


class MessageRetrieveView(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageListSerializer
    lookup_field = 'uid'
    permission_classes = [AllowAny]


class MessageListView(generics.ListAPIView):
    serializer_class = MessageListSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.is_staff:
            return Message.objects.filter(status='not answered').order_by('-uploaded_at')
        return Message.objects.filter(status='answered').order_by('-uploaded_at')



class MessageUpdateView(generics.UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageUpdateSerializer  # ✅ Use the update serializer
    lookup_field = 'uid'
    permission_classes = [IsAdminUser]  # ✅ Only admins can update messages

    def perform_update(self, serializer):
        """Ensure the status is set to 'answered' when an answer is provided."""
        instance = serializer.save()
        if instance.answer:
            instance.status = 'answered'
            instance.save()





class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



class CommentListAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsDoctorOrAdmin]


class CommentDeleteAPIView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsDoctorOrAdmin]
    lookup_field = 'uid'