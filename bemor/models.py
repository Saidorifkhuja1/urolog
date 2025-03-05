from django.db import models
from account.models import *
import uuid
from shifokor.models import Shifokor


class Bemor(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=1000)
    kasallik = models.TextField()
    tashxis = models.TextField()
    doctor = models.ForeignKey(Shifokor, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name




