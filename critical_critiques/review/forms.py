from django import forms

from submission.models import Submission

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = []