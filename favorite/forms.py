from django.forms import ModelForm
from favorite.models import FavoritedBooks

class FavoritedBookForm(ModelForm):
    class Meta:
        model = FavoritedBooks
        fields = ["alasan"]
    
    