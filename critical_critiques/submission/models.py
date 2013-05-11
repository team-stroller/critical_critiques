import datetime

from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User


class SubmissionManager(models.Manager):
    _expiry_time = datetime.timedelta(hours=2)

    def next_random_avoiding(self, user):
        not_self = ~Q(user=user)
        submission = Submission.objects.filter(not_self,status='new').order_by('?')[0]
        submission.active_for(user)
        return submission

    def expired(self):
        """Fetch Submissions with expired reviewers"""

        qs = self.get_query_set()
        expiration_date = datetime.datetime.now() - self._expiry_time
        return qs.filter(date_activated__lte=expiration_date, status='active')

    def expire_inactive(self):
        """Deactivate expired Submissions"""

        submissions = self.expired()
        submissions.update(status='new', date_activated=None, reviewer=None)

class Submission(models.Model):
    _status_options = (
        ('new', 'Ready to be picked up'),
        ('active', 'A reviewer has been assigned'),
        ('reviewed', 'Has been reviewed'),
    )

    user = models.ForeignKey(User)
    url = models.URLField()
    status = models.CharField(choices=_status_options, default='new',
                              max_length=15)
    date_activated = models.DateTimeField(default=None, blank=True,
                                          null=True)
    reviewer = models.ForeignKey(User, related_name='reviews', null=True)
    objects = SubmissionManager()

    def __unicode__(self):
        return str(self.url)

    def active_for(self, reviewer):
        now = datetime.datetime.now()
        self.reviewer = reviewer
        self.status = 'active'
        self.date_activated = now
        self.save()
