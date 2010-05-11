from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.contrib.auth.decorators import login_required

from django.views.generic.create_update import create_object
from django.views.generic.create_update import update_object
from django.views.generic.create_update import delete_object

from django.views.generic.list_detail import object_list, object_detail
from models import Mission

save_mission_dict = {
    'model': Mission,
    #'queryset': Mission.objects.all(),
    'post_save_redirect': '/missions/',
}

delete_mission_dict = {
    'model': Mission,
    #'queryset': Mission.objects.all(),
    'post_delete_redirect': '/missions/',
}

update_mission_dict = {
    'model': Mission,
    #'queryset': Mission.objects.all(),
    'post_save_redirect': '/missions/',
}

missions_dict = {
    'queryset': Mission.objects.all(),
}

urlpatterns = patterns('missions.views',
    (r'^$', object_list, missions_dict),
    (r'^new/', create_object, save_mission_dict),
    (r'^edit/(?P<object_id>\d+)/', update_object, update_mission_dict),
    (r'^delete/(?P<object_id>\d+)/', delete_object, delete_mission_dict),
    (r'^(?P<object_id>\d+)/', object_detail, missions_dict),
    #(r'^(?P<mission_id>\d+)', 'object_detail', {}),
    #(r'^new/', 'new'),
    #(r'^(?P<mission_id>\d+)/edit', 'edit'),
    #(r'^(?P<mission_id>\d+)', 'show'),
)
