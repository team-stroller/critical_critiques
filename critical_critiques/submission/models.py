from django.db import models
from django.contrib.auth.models import User

class Submission(models.Model):
  user = models.ForeignKey(User)
  url = models.URLField
