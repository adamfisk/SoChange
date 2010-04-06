import logging
import urllib
import urllib2
import sys
from django.utils import simplejson
import time

from ConfigParser import ConfigParser

class Expensify():
    
    BASE_URL = "https://wwwizardry.expensify.com/api?%s"
    
    authToken = ""
    
    authTime = 0
    
    def __init__(self):
        cfg = ConfigParser()
        cfg.read('config/sochange.properties')
        partnerName = cfg.get("config", "partnerName")
        email = cfg.get("config", "email")
        partnerUserID = cfg.get("config", "partnerUserID")
        partnerPassword = cfg.get("config", "partnerPassword")
        partnerUserSecret = cfg.get("config", "partnerUserSecret")
        aesIV = cfg.get("config", "aesIV")
        aesKey = cfg.get("config", "aesKey")
        
        self.baseArgs = {
            'partnerUserID': partnerUserID,
            'partnerPassword': partnerPassword,
            'partnerUserSecret': partnerUserSecret,
        }
        
    def newAuthCommandBase(self, commandName):
        if self.authToken is None or self.authToken == "":
            self.authenticate();
        args = self.newCommandBase(commandName)
        args['authToken'] = self.authToken
        return args

    def newCommandBase(self, commandName):
        args = self.baseArgs.copy()
        args['command'] = commandName
        return args
        
    def returnJson(self, args):
        url = self.BASE_URL % urllib.urlencode(args)
        logging.info("Accessing JSON using URL: %s", url)
        try:
            filehandle = urllib2.urlopen(url)
            body = filehandle.read()
            print body
            bodyJson = simplejson.loads(body)
            tok = bodyJson['authToken']
            if tok is not None and tok != "":
                self.authToken = tok
                self.authTime = time.time()
            return bodyJson
        except Exception, e:
            print "Unexpected error:", sys.exc_info()
        
    def authenticate(self):
        curTime = time.time()
        elapsed = curTime - self.authTime
        elapsedMinutes = elapsed / 60
        
        # The authentication tokens are good for 1 hour
        if elapsedMinutes < 58:
            logging.info("Not re-authenticating.\
                Our auth token is only "+str(elapsed)+" seconds old")
            return
        args = self.newCommandBase('Authenticate')
        self.returnJson(args)
        
    def get(self, list):
        args = self.newAuthCommandBase('Get')
        args['returnValueList'] = list
        self.returnJson(args)
        
    def getCardList(self):
        return self.get('cardList')
        
    def getTransactionList(self):
        return self.get('transactionList')