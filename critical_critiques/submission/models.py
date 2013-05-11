from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User


class SubmissionManager(models.Manager):
    def next_random_avoiding(self, user):
        not_self = ~Q(user=user)
        submission = Submission.objects.filter(not_self,status='new').order_by('?')[0]
        submission.active_for(user)
        return submission

class Submission(models.Model):
    _status_options = (
        ('new', 'New'),
        ('active', 'Active'),
        ('reviewed', 'Reviewed'),
    )

    user = models.ForeignKey(User)
    url = models.URLField()
    status = models.CharField(choices=_status_options, default='new',
                              max_length=15)
    reviewer = models.ForeignKey(User, related_name='reviews', null=True)
    objects = SubmissionManager()

    def __unicode__(self):
        return str(self.url)

    def active_for(self, reviewer):
        self.status = 'active'
        self.reviewer = reviewer
        self.save()
