from catalogue.models import Book
from django.forms import ModelForm

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','description','num_pages','avaliable']
