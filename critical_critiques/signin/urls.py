from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'signin.views.home', name='home'),
    url(r'^done$', 'signin.views.done', name='done'),
)
