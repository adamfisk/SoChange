from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse

def index(request):
    return render_to_response('users/index.html', context_instance=RequestContext(request))

def login(request):
    return HttpResponseRedirect(reverse('logged_in'))

def logged_in(request):
    return HttpResponse("All Logged In!!")
    

