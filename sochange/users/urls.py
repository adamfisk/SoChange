from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from users.views import user_page
from users.views import profile 
from users.views import home 
from users.views import user_profile 

urlpatterns = patterns('users.views',
    (r'^$', 'index'),
    #url(r'^$', 'index', name='user_index'),
    (r'^login/', 'login'),
    url(r'^logged_in$', 'logged_in', name='logged_in'),
    (r'^profile/', profile), 
    (r'^home/', home), 
    (r'^(\w+)/profile$', user_profile), #needs to be changed since it matches anything
    (r'^(\w+)/$', user_page), #needs to be changed since it matches anything

)
