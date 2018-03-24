from .base import *

import django_heroku
django_heroku.settings(locals())

# overwrite the django_heroku staticfiles
STATICFILES_STORAGE = "django_s3_storage.storage.StaticS3Storage"
