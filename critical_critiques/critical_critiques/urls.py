from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.views.static import serve
from django.conf import settings

from .views import LogoutView

# Enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name="home"),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Auth
    url(r'', include('social_auth.urls')),
    url(r'^logout/', LogoutView.as_view(), name="logout"),

    # Submission
    url(r'^submission/', include('submission.urls')),

    # Review
    url(r'^review/', include('review.urls')),

    # Static files
    url(r'^static/(?P<path>.*)$', serve,
        kwargs={'document_root':settings.STATIC_ROOT})
)
