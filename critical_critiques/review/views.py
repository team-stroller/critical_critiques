from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.http import Http404

from submission.models import Submission

from .forms import ReviewForm

class ReviewView(UpdateView):
    model = Submission
    template_name = 'create-review.html'
    form_class = ReviewForm
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        not_self = ~Q(user=self.request.user)
        try:
            submission = Submission.objects.filter(not_self,status='new').order_by('?')[0]
        except IndexError:
            # show empty state
            raise Http404
        return submission

    def form_valid(self, form):
        if form.is_valid():
            submission = form.save(commit=False)
            submission.status = 'reviewed'
            submission.save()
        return super(ReviewView, self).form_valid(form)