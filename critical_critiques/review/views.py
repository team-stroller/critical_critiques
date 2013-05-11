from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy
from django.http import Http404

from submission.models import Submission

from .forms import ReviewForm

class ReviewView(UpdateView):
    model = Submission
    template_name = 'create-review.html'
    form_class = ReviewForm
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        user = self.request.user
        try:
            return Submission.objects.next_random_avoiding(user)
        except IndexError:
            raise Http404

    def form_valid(self, form):
        if form.is_valid():
            submission = form.save(commit=False)
            submission.status = 'reviewed'
            submission.save()
        return super(ReviewView, self).form_valid(form)
