from rest_framework import generics
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
    serializer_class = MessageSerializer
    lookup_field = 'uid'
    permission_classes = [AllowAny]


class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer

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