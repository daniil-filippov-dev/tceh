# -*- coding: utf-8 -*-


DEBUG = False
SECRET_KEY = 'This key must be secret!'
# WTF_CSRF_ENABLED = False

try:
    from config_local import *
except ImportError:
    pass

