from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
#from social_auth.db.django_models import UserSocialAuth
#from github3.api import login
import logging

logger = logging.getLogger(__name__)

def dashboard(request):
  context = RequestContext(request)
  return render_to_response('dashboard.html', context)
