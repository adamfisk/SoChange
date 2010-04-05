"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
import logging
import urllib
import urllib2
from django.utils import simplejson
import time
import random
from Crypto.Cipher import AES
import binascii
import base64
import webbrowser
import sys

from ConfigParser import ConfigParser

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        #self.failUnlessEqual(1 + 1, 2)
        
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
        logging.info("Testing URL: %s", url)
        #webbrowser.open_new(url)
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
            
        
        """
        print partnerUserSecret
        
        expires = int(time.time()) + 60*5
        logging.info("Expires: %s", expires)
        ssoJson = simplejson.dumps({
            'arandom' : random.randint(0, 10000000),
            'expires' : expires, 
            'partnerPassword': partnerPassword,
            'partnerUserSecret': partnerUserSecret})
        
        # the block size for the cipher object; must be 16, 24, or 32 for AES
        BLOCK_SIZE = 16

        # the character used for padding--with a block cipher such as AES, the value
        # you encrypt must be a multiple of BLOCK_SIZE in length.  This character is
        # used to ensure that your value is always a multiple of BLOCK_SIZE
        PADDING = 'H'
        
        # one-liner to sufficiently pad the text to be encrypted
        pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
        
        key  = binascii.unhexlify(aesIV)
        IV   = binascii.unhexlify(aesKey)
        aes  = AES.new( key, AES.MODE_CBC, IV )
        sso = aes.encrypt(pad(ssoJson))
        #logging.info("SSO NON BASE 64: %s", sso)
        
        sso = base64.b64encode(sso)
        logging.info("SSO: %s", sso)
        
        ssoArgs = urllib.urlencode({
            'command' : 'Authenticate',
            'partnerUserID': partnerUserID,
            'sso' : sso,
        })
        """

            

__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}

