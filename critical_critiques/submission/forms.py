from django.forms import ModelForm, TextInput

from .models import Submission


class SubmissionForm(ModelForm):

    class Meta:
        model = Submission
        exclude = ('user', 'status', )
        widgets = {
          'url': TextInput(attrs={'placeholder': 'Paste a Github pull request URL'})
        }
