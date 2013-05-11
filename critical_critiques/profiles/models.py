from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name='profile')
    allowed_submissions = models.IntegerField(
        default=1, help_text=u'Number of requests user can submit')