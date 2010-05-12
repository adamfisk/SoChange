from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.contrib.auth.decorators import login_required

from django.views.generic.create_update import create_object
from django.views.generic.create_update import update_object
from django.views.generic.create_update import delete_object

from django.views.generic.list_detail import object_list, object_detail
from models import Campaign

campaign_create_dict = {
    'model': Campaign,
}

urlpatterns = patterns('campaigns.views',
    (r'^$', 'index'),
    (r'^new/', create_object, campaign_create_dict),
    (r'^(?P<object_id>[0-9]+)/edit', update_object, campaign_create_dict),
    #(r'^(?P<campaign_id>\d+)', 'object_detail', {}),
    #(r'^new/', 'new'),
    #(r'^(?P<campaign_id>\d+)/edit', 'edit'),
    #(r'^(?P<campaign_id>\d+)', 'show'),
)
