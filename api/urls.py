from django.conf.urls import patterns, url
from api.views import *
from rest_framework.authtoken import views as tokenView




print "api url"

urlpatterns = patterns('',
    url(r'^login/$', tokenView.obtain_auth_token),

    # url(r'^discussion/list/$',disccussions_list, name='disccussions-list'),
    # url(r'^comment/add/$',add_comment, name='comment-add'),
    # url(r'^discussion/details/$', discussion_search, name='search-discussion'),

    url(r'^discussion/list/$',ListDiscussions.as_view()),
    url(r'^comment/add/$',CreateCommentClass.as_view()),
    url(r'^discussion/details/$', SearchDiscussions.as_view()),




    #url(r'^discussion/details/(?P<title>.+)$', discussion_search, name='search-discussion'),
    # url(r'^discussion/details/(?P<title>[A-Za-z]+)/$', discussion_search, name='search-discussion'),
    # url(r'^discussion/details/$', views.discussion_search.as_view(), name='list')

)

