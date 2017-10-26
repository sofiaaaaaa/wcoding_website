from django.conf.urls import url

from . import views

urlpatterns = [
    # main post list views
    url(r'^$', views.post_list, name='post_list'),

    # program Learn More list views
    url(r'list', views.PostListView.as_view(), name='list'),

    # [-\w] : a word character (A-Za-z0-9_) or a dash(-) can go
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),

    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),

    # for taggit
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
]
