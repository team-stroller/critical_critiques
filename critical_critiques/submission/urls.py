from django.conf.urls import patterns, url
from .views import SubmissionView

urlpatterns = patterns('',
                       url(r'^$', SubmissionView.as_view()),
)
