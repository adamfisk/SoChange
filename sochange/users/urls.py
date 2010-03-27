from django.conf.urls.defaults import *

urlpatterns = patterns('sochange.users.views',
    (r'^$', 'index'),
)
