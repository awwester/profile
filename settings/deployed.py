from .local import *
import dj_database_url


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DATABASES = {}
DATABASES['default'] =  dj_database_url.config()
DATABASES['default']['CONN_MAX_AGE'] = 500

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'awwester'
EMAIL_HOST_PASSWORD = os.environ["EMAIL_HOST_PASSWORD"]
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# email that the contacts will be sent to
EMAIL_CONTACT = 'merainey15@gmail.com'
DEFAULT_FROM_EMAIL = 'Michael Rainey <%s>' % EMAIL_CONTACT
