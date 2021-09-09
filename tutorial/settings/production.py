# .production.py

from .base import *
import dj_database_url
import django_heroku


DEBUG =  os.environ.get('DJANGO_DEBUG', default='False')
ALLOWED_HOSTS = ['*']


DATABASES = {'default': dj_database_url.config()}


# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = BASE_DIR / 'staticfiles'

# The URL to use when referring to static files (where they will be served from)
STATIC_URL = '/static/'



STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(locals())


