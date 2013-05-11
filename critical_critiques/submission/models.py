from django.db import models
from django.contrib.auth.models import User


class Submission(models.Model):
    _status_options = (('new', 'New'), ('reviewed', 'Reviewed'),)

    user = models.ForeignKey(User)
    url = models.URLField()
    status = models.CharField(choices=_status_options, default='new',
                              max_length=15)

    def __unicode__(self):
        return str(self.url)
