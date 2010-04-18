from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^users/', include('users.urls')),
    (r'^admin/', include(admin.site.urls)),
    #(r'^accounts/', include('registration.backends.simple.urls')), # transition to default?
    (r'^accounts/', include('registration.backends.default.urls')),

)
