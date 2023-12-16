from donate.models import DonatedBook
from django.forms import ModelForm

class BookForm(ModelForm):
    class Meta:
        model = DonatedBook
        fields = ['title','author','description','num_pages']
