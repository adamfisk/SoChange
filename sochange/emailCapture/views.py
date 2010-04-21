from django.shortcuts import render_to_response
from emailCapture.models import EmailAddress
from emailCapture.models import EmailAddressForm

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt # temporary hack - probably should fix this
def index(request):
    if request.method == 'POST': # If the form has been submitted...
        form = EmailAddressForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            return render_to_response('emailCapture/thankyou.html') # Redirect after POST
    else:
        form = EmailAddressForm() # An unbound form

    return render_to_response('emailCapture/index.html', {
        'form': form,
    })

@csrf_exempt # temporary hack - probably should fix this
def thankyou(request):
    return render_to_response('emailCapture/thankyou.html')

