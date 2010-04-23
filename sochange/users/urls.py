from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from users.views import user_page
from users.views import profile 

urlpatterns = patterns('users.views',
    (r'^$', 'index'),
    #url(r'^$', 'index', name='user_index'),
    (r'^login/', 'login'),
    url(r'^logged_in$', 'logged_in', name='logged_in'),
    (r'^profile/', profile), 
    (r'^(\w+)/$', user_page), #needs to be changed since it matches anything

)
