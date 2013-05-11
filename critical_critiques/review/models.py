from django.db import models
from submission.models import Submission

class Review(models.Model):
    submission = models.ForeignKey(Submission)
    content = models.TextField()