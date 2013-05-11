from django.forms import ModelForm

class SubmissionForm(ModelForm):
  class Meta:
    model = Submission
    fields = ['url']
