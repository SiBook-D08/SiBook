from django.db import models
from catalogue.models import *
from django.contrib.auth.models import User
# Create your models here.
class GiveBack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review=models.TextField()
    date_added = models.DateField(auto_now_add=True)
    review_date=models.DateField(auto_now_add=True)