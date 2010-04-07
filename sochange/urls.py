from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^users/', include('sochange.users.urls')),
    (r'^admin/', include(admin.site.urls)),
)
