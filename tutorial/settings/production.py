# .production.py

from .base import *
import dj_database_url
#import django_heroku



#DEBUG =  os.environ.get('DJANGO_DEBUG', default='False')
DEBUG = True
ALLOWED_HOSTS = ['tutorialdav.herokuapp.com/','localhost', '127.0.0.1', '0.0.0.0']


DATABASES = {'default': dj_database_url.config()}


STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
STATICFILES_DIRS = ['static/']


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


#django_heroku.settings(locals())


