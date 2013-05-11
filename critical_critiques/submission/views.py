from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy

from .forms import SubmissionForm
from .models import Submission


class SubmissionView(CreateView):
    model = Submission
    template_name = "dashboard.html"
    form_class = SubmissionForm
    # Anton: Change the below to redirect to your review page
    success_url = reverse_lazy('create-review')

    def form_valid(self, form):
        if form.is_valid():
            submission = form.save(commit=False)
            submission.user = self.request.user
            submission.save()
        return super(SubmissionView, self).form_valid(form)
