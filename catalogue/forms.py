from django import forms

class EditBookForm(forms.Form):
    idBook = forms.IntegerField(label="Book's Id")
    description = forms.TextInput(label="Book's new description")