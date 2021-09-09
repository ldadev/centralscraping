# .production.py

from .base import *
import dj_database_url
import django_heroku


DEBUG =  os.environ.get('DJANGO_DEBUG', default='False')
ALLOWED_HOSTS = ['*']


DATABASES = {'default': dj_database_url.config()}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')

django_heroku.settings(locals())


