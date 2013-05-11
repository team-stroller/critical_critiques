from django import forms

from .models import Submission


class SubmissionForm(forms.ModelForm):

    class Meta:
        model = Submission
        exclude = ('user',)

    def clean_url(self):
        url = self.cleaned_data['url']
        # Pull Request: https://github.com/basho/webmachine/pull/143
        # Gist: https://gist.github.com/rmeritz/2863145
        if "github.com" not in url:
            raise forms.ValidationError(
                "Must be a URl for a github pull request")
        return url
