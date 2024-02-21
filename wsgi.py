"""
WSGI config for tokenProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

'''import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tokenProject.settings')

application = get_wsgi_application()'''
#!/usr/bin/env python


import os
from django.conf import settings
from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tokenProject.settings')

# Ensure settings are configured
if not settings.configured:
    settings.configure()

# Now you can import and use Django modules
import django
django.setup()
application = get_wsgi_application()


