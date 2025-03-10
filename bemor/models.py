from django.db import models
from account.models import *
import uuid
from django.utils import timezone
from shifokor.models import Shifokor


class Bemor(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=1000)
    sana = models.DateTimeField(default=timezone.now)
    tugilgan = models.DateTimeField(default=timezone.now)
    manzil = models.TextField()
    kasallik = models.TextField()
    anamnesis_m = models.TextField()
    anamnesis_v = models.TextField()
    praesens = models.TextField()
    tekshiruv = models.TextField()
    tashxis = models.TextField()
    tavsiya = models.TextField()
    doctor = models.CharField(max_length=500)
    mudir = models.CharField(max_length=500)
    def __str__(self):
        return self.name


