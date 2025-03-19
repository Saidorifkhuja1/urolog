
import uuid
from django.db import models


class ServicesCategory(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title




class Services(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    category = models.ForeignKey(ServicesCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=2000)
    type = models.CharField(max_length=2000)
    price_citizen = models.CharField(max_length=2000)
    price_foreign = models.CharField(max_length=2000)

