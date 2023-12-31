from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.TextField()
    author = models.TextField()
    description = models.TextField()
    num_pages = models.IntegerField()
    img_url = models.TextField(default="https://books.google.com/books/content?id=SXGCEAAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api")
    avaliable = models.BooleanField(default=True)
    favorited = models.BooleanField(default=False)
    last_edited_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
