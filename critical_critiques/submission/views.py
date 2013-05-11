from django.views.generic.edit import CreateView

from .forms import SubmissionForm
from .models import Submission


class SubmissionView(CreateView):
    model = Submission
    template_name = "dashboard.html"
    form_class = SubmissionForm

    def form_valid(self, form):
        if form.is_valid():
            form = form.save(commit=False)
            form.user = self.request.user
            form.save()
        return super(SubmissionView, self).form_valid(form)
