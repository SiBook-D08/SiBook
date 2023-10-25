from django.db import models
from django.conf import settings
from django.utils import timezone

class Book(models.Model):
    title = models.TextField()
    author = models.TextField()
    description = models.TextField()
    num_pages = models.IntegerField()
    img_url = models.TextField(default="https://books.google.com/books/content?id=SXGCEAAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api")
    avaliable = models.BooleanField(default=True)