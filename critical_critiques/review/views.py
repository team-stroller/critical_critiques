from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q

from submission.models import Submission

from .forms import ReviewForm

class ReviewView(UpdateView):
    model = Submission
    template_name = 'create-review.html'
    form_class = ReviewForm
    success_url = reverse_lazy('home')

    def get_form(self, form_class):
        form = super(ReviewView, self).get_form(form_class)

    def get_form_kwargs(self):
        """Extend the context with a random Submission"""

        kwargs = super(ReviewView, self).get_form_kwargs()
        if 'instance' not in kwargs or kwargs['instance'] is None:
            submission = (Submission.objects.filter(
                ~Q(user=self.request.user),
                status='new').order_by('?')[0])
            kwargs['instance'] = submission
        return kwargs

    def form_valid(self, form):
        if form.is_valid():
            submission = form.save(commit=False)
            submission.status = 'reviewed'
            submission.save()
        return super(ReviewView, self).form_valid(form)