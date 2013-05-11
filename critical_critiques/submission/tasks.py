import datetime

from celery.task import PeriodicTask

from models import Submission

class DeactivateExpiredSubmissions(PeriodicTask):
    run_every = datetime.timedelta(minutes=15)

    def run(self, *args, **kwargs):
        submissions = Submission.objects.expired()
        submissions.udpdate(status='new', date_activated=None)