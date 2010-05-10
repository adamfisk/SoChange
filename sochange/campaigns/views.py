from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext

def index(request):
    if request.method == 'POST':
        return create(request)
    else:
        return render_to_response('campaigns/index.html', context_instance=RequestContext(request))    

def create(request):
    return render_to_response("campaigns/create.html")
    
def new(request):
    return render_to_response("campaigns/new.html")
    
def show(request):
    return render_to_response("campaigns/show.html")
    
def edit(request):
    return render_to_response("campaigns/edit.html")
    
