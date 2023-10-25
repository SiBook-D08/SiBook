from django.forms import ModelForm
from borrow.models import Request

class ProductForm(ModelForm):
    class Meta:
        model = Request
        fields = ["title", "author"]