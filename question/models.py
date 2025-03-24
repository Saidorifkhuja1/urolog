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
    answer = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title




class Comment(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=500)
    family_name = models.TextField(max_length=500)
    body = models.TextField()
    old = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)


    def __str__(self):
        return self.name
