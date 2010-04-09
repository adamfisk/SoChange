from djangoappengine.settings_base import *

SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc4((7yd0dbrakhvi'

INSTALLED_APPS = (
    'users',
    'expensify',
    'registration',
    'djangoappengine',
    'djangotoolbox',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
)

ACCOUNT_ACTIVATION_DAYS = 7 # variable required for registration app

ADMIN_MEDIA_PREFIX = '/media/admin/'

import os
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)
