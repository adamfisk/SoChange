from django.shortcuts import render_to_response
from emailCapture.forms import EmailCaptureForm

from django.views.decorators.csrf import csrf_exempt

def index(request):
    if request.method == 'POST': # If the form has been submitted...
        form = EmailCaptureForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = EmailCaptureForm() # An unbound form

    return render_to_response('emailCapture/index.html', {
        'form': form,
    })

@csrf_exempt # temporary hack - probably should fix this
def thankyou(request):
    return render_to_response('emailCapture/thankyou.html')

