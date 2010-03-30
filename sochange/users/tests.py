"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
import logging
import urllib

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 2)
        logging.info("Testing URL!!!")
        """
        url = "https://wwwizardry.expensify.com/partnerSignin?\
            partnerPassword=42eab22f02449d51b267&\
            email=michaelnorman22@gmail.com&\
            partnerUserID=michaelnorman22@gmail.com&\
            partnerUserSecret=sanshou22"
        """
        url = "https://api.expensify.com?\
            command=Authenticate&\
            partnerName=wwwizardry&\
            partnerPassword=42eab22f02449d51b267&\
            partnerUserID=michaelnorman22@gmail.com&\
            partnerUserSecret=sanshou22&\
            useExpensifyLogin=true"
        filehandle = urllib.urlopen(url)
        print filehandle.read()

__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}

