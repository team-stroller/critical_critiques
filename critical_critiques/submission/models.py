import datetime

from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User


class SubmissionManager(models.Manager):
    def next_random_avoiding(self, user):
        not_self = ~Q(user=user)
        submission = Submission.objects.filter(not_self,status='new').order_by('?')[0]
        submission.active
        return submission

    def expired(self):
        """Fetch Submissions with expired reviewers"""

        qs = self.get_query_set()
        expiration_date = datetime.datetime.now() - Submission._expiry_time
        return qs.filter(date_activated__lte=expiration_date)

class Submission(models.Model):
    _expiry_time = datetime.timedelta(hours=2)
    _status_options = (
        ('new', 'New'),  # should get picked up
        ('active', 'Active'),  # a reviewer is assigned
        ('reviewed', 'Reviewed'),  # has been reviewed
    )

    user = models.ForeignKey(User)
    url = models.URLField()
    status = models.CharField(choices=_status_options, default='new',
                              max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    date_activated = models.DateTimeField(default=None, blank=True,
                                          null=True)
    objects = SubmissionManager()

    def __unicode__(self):
        return str(self.url)

    def active(self):
        now = datetime.datetime.now()
        # TODO: set reviewer=User
        self.update(status='active', date_activated=now)

    def deactivate(self):
        """
        Resets the Submission to its original state. Logic need to be in
        sync with tasks.DeactivateExpiredSubmissions

        """

        # TODO: set reviewer=None
        self.update(status='new', date_activated=None)