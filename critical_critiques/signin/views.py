from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from social_auth.db.django_models import UserSocialAuth
from github3.api import login
import logging

logger = logging.getLogger(__name__)

def home(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('done')
    else:
        return render_to_response('home.html', RequestContext(request))


def done(request):
    # user = request.user
    # logger.debug("THING")
    # logger.debug(user)
    # social_auth = UserSocialAuth.objects.get(user=user.pk)
    # tokens = social_auth.tokens
    # github = login(token=tokens['access_token'])
    # gists = [g for g in github.iter_gists()]
    return render_to_response('done.html', RequestContext(request))
