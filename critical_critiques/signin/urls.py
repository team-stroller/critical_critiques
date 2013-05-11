from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'signin.views.home', name='home'),
    url(r'^done$', 'signin.views.done', name='done'),
)
