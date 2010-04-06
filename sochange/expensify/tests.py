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
        #partnerName = cfg.get("config", "partnerName")
        #email = cfg.get("config", "email")
        #aesIV = cfg.get("config", "aesIV")
        #aesKey = cfg.get("config", "aesKey")
        
        partnerPassword = cfg.get("config", "partnerPassword")
        partnerUserID = cfg.get("config", "partnerUserID")
        partnerUserSecret = cfg.get("config", "partnerUserSecret")
        
        api = Expensify(partnerUserID, partnerUserSecret)
        api.createAccount('afisk@littleshoot.org')
        #api.getTransactionList()
        #api.getCardList()
        #api.authenticate()



