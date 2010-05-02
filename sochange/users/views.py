from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

import logging

@login_required
def index(request):
    logging.info("Rendering index")
    return render_to_response('users/home.html', context_instance=RequestContext(request))

@login_required
def user_page(request, username):
    try:
       user = User.objects.get(username=username)
    except:
       raise Http404('Requested user not found.')
    template = get_template('users/home.html')
    variables = RequestContext(request, {
       'user' : user,
       'username': username,
    })
    output = template.render(variables)
    return HttpResponse(output)

@login_required
def user_profile(request, username):
    try:
       user = User.objects.get(username=username)
    except:
       raise Http404('Requested user not found.')
    template = get_template('users/profile.html')
    variables = RequestContext(request, {
       'user' : user,
       'username': username,
    })
    output = template.render(variables)
    return HttpResponse(output)


@login_required
def profile(request):
    return render_to_response('users/profile.html', context_instance=RequestContext(request))

@login_required
def home(request):
    return render_to_response('users/home.html', context_instance=RequestContext(request))

