from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',
    #(r'^$', direct_to_template, {'template': 'index.html'}),
    url(r'^$', 'users.views.index', name='users_index'),
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^about/', include('emailCapture.urls')), # temporary email collector
    (r'^users/', include('users.urls')),
    (r'^admin/', include(admin.site.urls)),
    #(r'^accounts/', include('registration.backends.simple.urls')), # transition to default?
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^campaigns/', include('campaigns.urls')),

)
