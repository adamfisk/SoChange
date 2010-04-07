"""
Test for the Expensify API module.
"""

from django.test import TestCase
from ConfigParser import ConfigParser
import logging

from expensify_api import Expensify

class ApiTest(TestCase):
    def test_api(self):
        cfg = ConfigParser()
        cfg.read('config/sochange.properties')
        
        partnerPassword = cfg.get("config", "partnerPassword")
        partnerUserID = cfg.get("config", "partnerUserID")
        partnerUserSecret = cfg.get("config", "partnerUserSecret")
        
        api = Expensify(partnerUserID, partnerUserSecret)
        authJson = api.authenticate()
        accountJson = api.createAccount('afisk@littleshoot.org')
        
        # This account should already exist, returning 300
        self.failUnlessEqual(accountJson['jsonCode'], 300)
        
        transactionJson = api.getTransactionList()
        self.failUnless('transactionList' in transactionJson, 'No transaction list')

        cardJson = api.getCardList()
        self.failUnless('cardList' in cardJson, 'No card list')



