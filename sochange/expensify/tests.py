"""
Test for the Expensify API module.
"""

from django.test import TestCase
from ConfigParser import ConfigParser
import logging
import os

import models
from expensify_api import Expensify
from django.contrib.auth.models import User

class ApiTest(TestCase):
        
    def test_api(self):
        cfg = ConfigParser()
        props = os.path.join(os.path.dirname(__file__), 'sochange.properties')
        cfg.read(props)
        
        partnerPassword = cfg.get("config", "partnerPassword")
        partnerUserID = cfg.get("config", "partnerUserID")
        partnerUserSecret = cfg.get("config", "partnerUserSecret")
        
        api = Expensify(partnerUserID, partnerUserSecret)
        
        logging.info("Authenticating")
        authJson = api.authenticate()
        
        logging.info("Creating account")
        accountJson = api.createAccount('michaelnorman22@gmail.com')
        
        logging.info("JSON: %s", accountJson)
        # This account should already exist, returning 300 
        self.failUnlessEqual(accountJson['jsonCode'], 300)
        
        transactionJson = api.getTransactionList()
        self.failUnless('transactionList' in transactionJson, 'No transaction list')

        cardJson = api.getCardList()
        self.failUnless('cardList' in cardJson, 'No card list')
        
    def test_activation_handler(self):
        new_user = User.objects.create_user('test', 'test@test.org', 'test')
        
        # Tricky to test here because the handler method can't return -- if it
        # does whatever it returns is displayed straight in the UI.
        models.activation_handler(sender=self.__class__,
                                  user=new_user,
                                  request=None)
        #self.failUnlessEqual(json['jsonCode'], 300)



