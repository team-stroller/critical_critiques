from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    due_reviews = models.IntegerField(u'Due reviews', default=2,
                                      help_text=u'Number of reviews user can '
                                                u'create')