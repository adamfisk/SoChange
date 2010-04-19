from django.db import models

from django.contrib.auth.models import User
import registration.signals
from expensify_api import Expensify
import logging

def activation_handler(sender, user, request, **kwargs):
    logging.info('Got user activated signal!!')
    if not user:
        logging.error('No user??')
        return
    
    email = getattr(user, 'email')
    logging.info('Got email: %s', email)
    
    expensify = Expensify()
    expensify.createAccount(email)
    #json = expensify.createAccount(email)
    #logging.info('Got JSON: %s', json)
    #if json['jsonCode'] is 200:
    #    logging.info('Successfully created user. Email should be sent')
    #else:
    #    logging.error('Could not create user!!')
    
registration.signals.user_activated.connect(activation_handler)


