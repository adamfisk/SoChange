from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.forms import ModelForm

from models import Mission

import logging

class MissionForm(ModelForm):
    class Meta:
        model = Mission

def index(request):
    if request.method == 'POST':
        return create(request)
    else:
        return render_to_response('missions/index.html', context_instance=RequestContext(request))    

def create(request):
    form = MissionForm(request.POST)
    if form.is_valid():
        campaign = form.save(commit=True)
        return HttpResponseRedirect(reverse('show', args=[campaign]))
    return HttpResponse("Invalid campaign")
    #return render_to_response("campaigns/create.html", context_instance=RequestContext(request))
    
def new(request):
    return render_to_response("missions/new.html", context_instance=RequestContext(request))
    
def show(request, campaign_id):
    logging.info("Mission ID: %s", campaign_id)
    try:
        c = Mission.objects.get(pk=campaign_id)
    except Mission.DoesNotExist:
        raise Http404
    return render_to_response("missions/show.html", {'campaign': c}, context_instance=RequestContext(request))
    
def edit(request, campaign_id):
    logging.info("Mission ID: %s", campaign_id)
    try:
        c = Mission.objects.get(pk=campaign_id)
    except Mission.DoesNotExist:
        raise Http404
    return render_to_response("missions/edit.html", {'campaign': c}, context_instance=RequestContext(request))
    
