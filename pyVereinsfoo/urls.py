from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pyVereinsfoo.views.home', name='home'),
    # url(r'^pyVereinsfoo/', include('pyVereinsfoo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('dashboard.urls')),
    url(r'^members/', include('members.urls')),
    url(r'^user/', include('userauth.urls')),
)
