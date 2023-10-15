from django.db import models
from django.conf import settings
from django.utils import timezone

class Book(models.Model):
    title = models.TextField()
    author = models.TextField()
    description = models.TextField()
    num_pages = models.IntegerField()
    avaliable = models.BooleanField(default=True)