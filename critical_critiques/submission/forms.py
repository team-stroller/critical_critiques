from urlparse import urlparse

from django import forms
from django.forms import ModelForm

from .models import Submission


class SubmissionForm(ModelForm):

    class Meta:
        model = Submission
        exclude = ('user', 'status', 'reviewer')

    def clean_url(self):
        url = self.cleaned_data['url']
        parsed_url = urlparse(url)
        if not (parsed_url.scheme == 'https'):
            raise forms.ValidationError("Must be a https")
        if parsed_url.params or parsed_url.query or parsed_url.fragment:
            self._raise_url_error()
        domain = parsed_url.netloc
        path = parsed_url.path.split('/')
        if domain == "github.com":
            return self._clean_pull_request_url(url, path)
        if domain == "gist.github.com":
            return self._clean_gist_url(url, path)
        else:
            self._raise_url_error()

    # Valid Gist: https://gist.github.com/rmeritz/2863145
    def _clean_gist_url(self, url, path):
        if not (self._is_valid_url_length(3, path)
                and self._path_has_id(path, 2)):
            self._raise_url_error()
        return url

    # Valid Pull Request: https://github.com/basho/webmachine/pull/143
    def _clean_pull_request_url(self, url, path):
        if not (self._is_valid_url_length(5, path) and
                self._path_has_id(path, 4) and
                (path[3] == 'pull')):
            self._raise_url_error()
        return url

    def _is_valid_url_length(self, length, path):
        return (((len(path) == length) or
                 (len(path) == (length + 1) and path[length] == '')) and
                (path[0] == ''))

    def _path_has_id(self, path, index):
        return path[index].isdigit()

    def _raise_url_error(self):
        raise forms.ValidationError("Must be a valid Github Pull Request URL")
