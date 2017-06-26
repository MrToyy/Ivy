"""
WSGI config for ivybridge project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
#import sys

#sys.path.append('/opt/bitnami/apps/django/django_projects/IvyBridge')
#os.environ.setdefault("PYTHON_EGG_CACHE", "/opt/bitnami/apps/django/django_projects/IvyBridge/egg_cache")

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ivybridge.settings")

application = get_wsgi_application()
