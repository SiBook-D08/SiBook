from django import forms

class FavoritedBookForm(forms.Form):
    alasan = forms.CharField(max_length=255)

    def clean_alasan(self):
        alasan = self.cleaned_data.get('alasan')
        if not alasan:
            raise forms.ValidationError("Wajib diisi!")
        return alasan
    