from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('users.views',
    #(r'^$', direct_to_template, {'template': 'users/index.html'}),
    #(r'^$', direct_to_template, {'template': 'users/index.html'}),
    #url(r'^$', 'index', name='user_index'),
    url(r'^login/', 'user_login', name='login'),
    #(r'^login_required_test/', 'login_required_test'),
    #url(r'^logged_in$', 'logged_in', name='logged_in'),
    (r'^profile/', 'profile'), 
    (r'^home/', 'home'), 
    (r'^(\w+)/profile$', 'user_profile'), #needs to be changed since it matches anything
    (r'^(\w+)/$', 'user_page'), #needs to be changed since it matches anything

)
