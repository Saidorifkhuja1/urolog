import uuid
from django.utils import timezone
from django.db import models

class Message(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=500)
    body = models.TextField()
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Answer(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    body = models.TextField()
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


