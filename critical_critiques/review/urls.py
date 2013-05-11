from django.conf.urls import patterns, url
from .views import ReviewView

urlpatterns = patterns(
    '',
    url(r'^$', ReviewView.as_view(), name='create-review'),
)
