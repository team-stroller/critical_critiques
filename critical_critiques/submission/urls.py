from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'submission.views.dashboard', name='dashboard'),
)
