from django import forms

class reviewBookForm(forms.Form):
    review = forms.CharField(widget=forms.Textarea)

    def clean_review(self):
        review = self.cleaned_data.get('review')
        return review
    