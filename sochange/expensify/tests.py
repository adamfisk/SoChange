"""
Test for the Expensify API module.
"""

from django.test import TestCase
import logging

from expensify_api import Expensify

class ApiTest(TestCase):
    def test_api(self):
        api = Expensify();
        api.authenticate();



