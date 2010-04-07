import logging
import urllib
import urllib2
from urllib2 import HTTPError
import sys
from django.utils import simplejson
import time

from ConfigParser import ConfigParser

"""
 Class for interacting with the Expensify API.
"""
class Expensify():
    
    authToken = ""
    authTime = 0
    
    def __init__(self, partnerUserID, partnerUserSecret):
        cfg = ConfigParser()
        cfg.read('config/sochange.properties')
        
        self.partnerPassword = cfg.get("config", "partnerPassword")
        self.partnerName = cfg.get("config", "partnerName")
        self.BASE_URL = "https://" + self.partnerName + ".expensify.com/api?%s"
        
        self.baseArgs = {
            'partnerPassword': self.partnerPassword,
            'partnerUserID': partnerUserID,
            'partnerUserSecret': partnerUserSecret,
        }
                
    def getCardList(self):
        return self.get('cardList')
        
    def getTransactionList(self):
        return self.get('transactionList')
        
    def createAccount(self, email):
        logging.info('Creating account')
        args = {
            'partnerPassword': self.partnerPassword,
            'command' : 'CreateAccount',
            'email' : email,
            'referer' : 'test',
        }
        # If we get a 300-level response here, it means the account already
        # exists.
        return self.__returnJson(args)
    
    def get(self, list):
        args = self.__newAuthCommandBase('Get')
        args['returnValueList'] = list
        return self.__returnJson(args)
        
    def authenticate(self):
        logging.info("Authenticating")
        curTime = time.time()
        elapsed = curTime - self.authTime
        elapsedMinutes = elapsed / 60
        
        # The authentication tokens are good for 1 hour
        if elapsedMinutes < 58:
            logging.info("Not re-authenticating.\
                Our auth token is only "+str(elapsed)+" seconds old")
            return
        args = self.__newCommandBase('Authenticate')
        
        """
        Special response codes for authentication:
        401 Password is wrong.
        404 Account not found.
        405 Email not validated.
        """
        return self.__returnJson(args)
        
    def __newAuthCommandBase(self, commandName):
        if self.authToken is None or self.authToken == "":
            self.authenticate();
        args = self.__newCommandBase(commandName)
        args['authToken'] = self.authToken
        return args

    def __newCommandBase(self, commandName):
        args = self.baseArgs.copy()
        args['command'] = commandName
        return args
        
    def __returnJson(self, args):
        url = self.BASE_URL % urllib.urlencode(args)
        logging.info("Accessing JSON using URL: %s", url)
        try:
            filehandle = urllib2.urlopen(url)
            body = filehandle.read()
            print body
            bodyJson = simplejson.loads(body)
            if 'authToken' in bodyJson:
                tok = bodyJson['authToken']
                if tok is not None and tok != "":
                    self.authToken = tok
                    self.authTime = time.time()
            else:
                logging.info("No auth token returned")
            return bodyJson
        except HTTPError, e:
            print e.code, e.msg
            print "HTTP error:", sys.exc_info()
        except Exception, e:
            print "Unexpected error:", sys.exc_info()