from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny,IsAdminUser

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
    queryset = Message.objects.all().order_by('-uploaded_at')
    serializer_class = MessageSerializer
    permission_classes = [AllowAny]


class AnswerCreateView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        answer = serializer.save()  # Save the answer instance

        # # Update the related message's status to "answered"
        # message = answer.message
        # message.status = "answered"
        # message.save()

class AnswerRetrieveView(generics.RetrieveAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    lookup_field = 'uid'
    permission_classes = [AllowAny]

class AnswerUpdateView(generics.UpdateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    lookup_field = 'uid'
    permission_classes = [IsAdminUser]

class AnswerDeleteView(generics.DestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    lookup_field = 'uid'
    permission_classes = [IsAdminUser]

class AnswerListView(generics.ListAPIView):
    queryset = Answer.objects.all().order_by('-uploaded_at')
    serializer_class = AnswerSerializer
    permission_classes = [AllowAny]