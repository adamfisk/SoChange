from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext

from models import Campaign

import logging

class CampaignForm(djangoforms.ModelForm):
    class Meta:
        model = Campaign

def index(request):
    if request.method == 'POST':
        return create(request)
    else:
        return render_to_response('campaigns/index.html', context_instance=RequestContext(request))    

def create(request):
    form = CampaignForm(request.POST)
    if form.is_valid():
        campaign = form.save(commit=True)
        return HttpResponseRedirect(reverse('show', args=[campaign]))
    return HttpResponse("Invalid campaign")
    #return render_to_response("campaigns/create.html", context_instance=RequestContext(request))
    
def new(request):
    return render_to_response("campaigns/new.html", context_instance=RequestContext(request))
    
def show(request, campaign_id):
    logging.info("Campaign ID: %s", campaign_id)
    try:
        c = Campaign.objects.get(pk=campaign_id)
    except Campaign.DoesNotExist:
        raise Http404
    return render_to_response("campaigns/show.html", {'campaign': c}, context_instance=RequestContext(request))
    
def edit(request, campaign_id):
    logging.info("Campaign ID: %s", campaign_id)
    try:
        c = Campaign.objects.get(pk=campaign_id)
    except Campaign.DoesNotExist:
        raise Http404
    return render_to_response("campaigns/edit.html", {'campaign': c}, context_instance=RequestContext(request))
    
