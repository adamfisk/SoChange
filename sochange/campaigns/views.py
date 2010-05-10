from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext

import logging

def index(request):
    if request.method == 'POST':
        return create(request)
    else:
        return render_to_response('campaigns/index.html', context_instance=RequestContext(request))    

def create(request):
    return render_to_response("campaigns/create.html", context_instance=RequestContext(request))
    
def new(request):
    return render_to_response("campaigns/new.html", context_instance=RequestContext(request))
    
def show(request, campaignId):
    logging.info("Campaign ID: %s", campaignId)
    return render_to_response("campaigns/show.html", context_instance=RequestContext(request))
    
def edit(request, campaignId):
    logging.info("Campaign ID: %s", campaignId)
    return render_to_response("campaigns/edit.html", context_instance=RequestContext(request))
    
