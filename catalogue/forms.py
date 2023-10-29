from django import forms

class EditBookForm(forms.Form):
    idBook = forms.IntegerField()
    description = forms.TextInput()