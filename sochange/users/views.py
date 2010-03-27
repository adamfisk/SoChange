from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

def index(request):
    #return HttpResponse("Hello, world. You're at the poll index.")
    return render_to_response('users/index.html', context_instance=RequestContext(request))
