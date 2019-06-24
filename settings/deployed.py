from .base import *

import django_heroku
django_heroku.settings(locals())

# overwrite the django_heroku staticfiles
STATICFILES_STORAGE = "django_s3_storage.storage.StaticS3Storage"


AWS_S3_BUCKET_NAME = os.environ.get('BUCKETEER_BUCKET_NAME')
AWS_S3_BUCKET_NAME_STATIC = AWS_S3_BUCKET_NAME
AWS_REGION = "us-east-1"
AWS_ACCESS_KEY_ID = os.environ.get('BUCKETEER_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('BUCKETEER_AWS_SECRET_ACCESS_KEY')
