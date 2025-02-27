from django.db import models
from account.models import *
import uuid


class Bemor(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=1000)
    kasallik = models.TextField()
    tashxi = models.TextField()
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




