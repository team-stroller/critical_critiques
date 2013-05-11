from django.contrib.auth import logout
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse


class LogoutView(RedirectView):
    url = "/"

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
