"""
WSGI config for adam project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

settings_file = os.environ["SETTINGS_FILE"]
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_file)

application = get_wsgi_application()

if settings_file == "settings.deployed":
    application = DjangoWhiteNoise(application)
