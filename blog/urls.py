from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<post_id>[0-9]+)/$', views.view, name='view'),
    url(r'^profile/$', views.profile, name='profile'),

]
