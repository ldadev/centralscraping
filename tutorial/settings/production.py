# .production.py

from .base import *
import dj_database_url
import django_heroku


DEBUG =  os.environ.get('DJANGO_DEBUG', default='False')
ALLOWED_HOSTS = ['*']


DATABASES = {'default': dj_database_url.config()}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(locals())


