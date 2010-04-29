from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

import logging

def index(request):
    logging.info("Rendering index")
    return render_to_response('users/index.html', context_instance=RequestContext(request))
    
    
@login_required
def login_required_test(request):
    return HttpResponse("@login_required seems to work!!")

def user_login(request):
    logging.info('Got login!!')
    #return HttpResponseRedirect(reverse('logged_in'))
    username = request.POST['username']
    password = request.POST['password']
    logging.info("User:  %s", username)
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect(reverse('login'))
        else:
            # Return a 'disabled account' error message
            return HttpResponse("Not active?")
    else:
        # Return an 'invalid login' error message.
        return HttpResponse("Hmnnn...no go!!")

#def logged_in(request):
#    logging.info('Got logged in!!')
#    return HttpResponse("All Logged In!!")

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

 
def profile(request):
    return render_to_response('users/profile.html')

def home(request):
    return render_to_response('users/home.html')

