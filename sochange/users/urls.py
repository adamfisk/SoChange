from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('sochange.users.views',
    (r'^$', 'index'),
    #url(r'^$', 'index', name='user_index'),
    (r'^login/', 'login'),
    url(r'^logged_in$', 'logged_in', name='logged_in'),
)
