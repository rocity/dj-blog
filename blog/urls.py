from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>[0-9]+)/$', views.view, name='view'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/posts/$', views.user_posts, name='user_posts'),
    url(r'^commentstatus/$', views.change_comment_status, name='change_comment_status'),

    url(r'^comments/$', views.postcomments, name='postcomments'),
    url(r'^new/$', views.newpost, name='new'),
    url(r'^posts/tag/(?P<slug>[\w-]+)$', views.posts_by_tag, name='postsbytag'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout')
]
