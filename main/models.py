from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    publishDate = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    page_count = models.IntegerField()
