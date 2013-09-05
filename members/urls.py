from django.conf.urls import patterns, include, url

from members.views import MemberDetailView, MemberListView

urlpatterns = patterns('members.views',
    url(r'^search/$', 'search'),
    url(r'^create/$', 'create', name='members_member_create'),
#    url(r'^edit/(?P<member_id>\d+)/$', 'edit', name='members_member_edit'),
)

urlpatterns += patterns('',
    url(r'^member/(?P<slug>[-\w]+)/$', MemberDetailView.as_view(),
        name='members_member_detail'),
    url(r'^$', MemberListView.as_view(), name='members_member_index'),
)
