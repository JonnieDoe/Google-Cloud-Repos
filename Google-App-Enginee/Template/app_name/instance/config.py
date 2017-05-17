"""
Variables defined in the instance/config.py file can override the value in conf.cfg
KEEP THIS FILE OUTSIDE OF GIT REPOS

To generate new secret key:
    import os
    os.urandom(24)

SECRET_KEY = '\xbb\x8f%\xccaX\r\x19\t)\xca\x14>u\x99-\x93\xcc\xc3Zw~\x95\x7f'
"""

import os


SECRET_KEY = os.urandom(24)
SESSION_SECRET_KEY = SECRET_KEY
SESSION_TYPE = 'memcached'
