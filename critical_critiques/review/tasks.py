from django.core.mail import send_mail

from celery.task import task

from submission.models import Submission

@task
def notify_author(submission_id):
    from_email = "stroller@codevalley.com"
    submission = Submission.objects.select_related('user').get(id=submission_id)
    recipients = [submission.user.email]
    subject = "Your submission has been reviewed!"
    message = "Go check it out at %s" % submission.url
    send_mail(subject, message, from_email, recipients, fail_silently=False)