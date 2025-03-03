import uuid
from django.db import models
from account.models import User

class Category(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title




class Shifokor(User):
    # uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()

