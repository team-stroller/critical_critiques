from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.views.static import serve
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),

    # Examples:
    # url(r'^$', 'critical_critiques.views.home', name='home'),
    # url(r'^critical_critiques/', include('critical_critiques.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Auth
    url(r'', include('social_auth.urls')),
    url(r'^signin/', include('signin.urls')),

    # Static files
    url(r'^static/(?P<path>.*)$', serve,
        kwargs={'document_root':settings.STATIC_ROOT})
)