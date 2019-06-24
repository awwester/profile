from .base import *

import django_heroku
django_heroku.settings(locals())


# Static and uploaded file storage
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


AWS_STORAGE_BUCKET_NAME = os.environ.get('BUCKETEER_BUCKET_NAME')
AWS_S3_REGION_NAME = os.environ.get('BUCKETEER_AWS_REGION')
AWS_ACCESS_KEY_ID = os.environ.get('BUCKETEER_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('BUCKETEER_AWS_SECRET_ACCESS_KEY')
