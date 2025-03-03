import uuid
from django.utils import timezone
from django.db import models

class Message(models.Model):
    STATUS_CHOICES = [
        ('answered', 'Answered'),
        ('not answered', 'Not Answered'),
    ]
    uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=500)
    body = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='not answered')
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


