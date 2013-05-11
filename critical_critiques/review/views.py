from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy

from submission.models import Submission

from .models import Review
from .forms import ReviewForm

class ReviewView(CreateView):
    model = Review
    template_name = 'create-review.html'
    form_class = ReviewForm
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        """Extend the context with a random Submission"""

        kwargs = super(ReviewView, self).get_form_kwargs()
        submission = Submission.objects.filter(status='new').order_by('?')[0]
        kwargs['initial']['submission'] = submission
        return kwargs

    def form_valid(self, form):
        if form.is_valid():
            review = form.save(commit=False)
            review.user = self.request.user
            review.save()
        return super(ReviewView, self).form_valid(form)