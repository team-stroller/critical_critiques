import datetime

from celery.task import PeriodicTask

from models import Submission

class DeactivateExpiredSubmissions(PeriodicTask):
    run_every = datetime.timedelta(minutes=15)

    def run(self, *args, **kwargs):
        Submission.objects.expire_inactive()
        