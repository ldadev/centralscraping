# .production.py

from .base import *
import dj_database_url
import django_heroku


DEBUG =  os.environ.get('DJANGO_DEBUG', default='True')
ALLOWED_HOSTS = ['*']


DATABASES = {'default': dj_database_url.config()}

STATIC_ROOT = os.path.join(BASE_DIR,'static')

STATIC_URL = '/static/'


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(locals())