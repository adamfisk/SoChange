from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.template.loader import get_template

def index(request):
    return render_to_response('users/index.html', context_instance=RequestContext(request))

def login(request):
    return HttpResponseRedirect(reverse('logged_in'))

def logged_in(request):
    return HttpResponse("All Logged In!!")

def user_page(request, username):
  try:
     user = User.objects.get(username=username)
  except:
     raise Http404('Requested user not found.')
  template = get_template('users/user_page.html')
  variables = RequestContext(request, {
     'username': username,
  })
  output = template.render(variables)
  return HttpResponse(output)
 
def profile(request):
    return render_to_response('users/profile.html')

