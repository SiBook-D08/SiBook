from catalogue.models import Book
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DonatedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.TextField()
    author = models.TextField()
    description = models.TextField()
    num_pages = models.IntegerField()
    last_edited_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, commit=True):
        if commit:
            new_book = Book(
                title=self.title,
                author=self.author,
                description=self.description,
                num_pages=self.num_pages,
                last_edited_user=self.last_edited_user
            )
            self.book = new_book
            self.book.save()
        return super().save(commit)
