import logging
import urllib
import urllib2
from django.utils import simplejson

from ConfigParser import ConfigParser

class Expensify():
    def authenticate(self):
        cfg = ConfigParser()
        cfg.read('config/sochange.properties')
        partnerName = cfg.get("config", "partnerName")
        email = cfg.get("config", "email")
        partnerUserID = cfg.get("config", "partnerUserID")
        partnerPassword = cfg.get("config", "partnerPassword")
        partnerUserSecret = cfg.get("config", "partnerUserSecret")
        aesIV = cfg.get("config", "aesIV")
        aesKey = cfg.get("config", "aesKey")
        
        args = urllib.urlencode({
            'command' : 'Authenticate',
            'partnerUserID': partnerUserID,
            'partnerPassword': partnerPassword,
            'partnerUserSecret': partnerUserSecret,
        })
        
        url = "https://wwwizardry.expensify.com/api?%s" % args
        logging.info("Logging in using URL: %s", url)
        try:
            filehandle = urllib2.urlopen(url)
            body = filehandle.read()
            print body
            bodyJson = simplejson.loads(body)
            authToken = bodyJson['authToken']
            print authToken
        except Exception, e:
            #print e.code
            #print e.read()
            print "Unexpected error:", sys.exc_info()