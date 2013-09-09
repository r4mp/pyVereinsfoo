from django.conf.urls import patterns, include, url

urlpatterns = patterns('dashboard.views',
            url(r'^$', 'index', name='dashboard_dasboard_index'),
)
