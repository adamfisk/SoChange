from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext

def campaign_view(request):
    return render_to_response('campaigns/campaign.html', context_instance=RequestContext(request))
