from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^users/', include('sochange.users.urls')),
)
