# .production.py

from .base import *
import dj_database_url
#import django_heroku



#DEBUG =  os.environ.get('DJANGO_DEBUG', default='False')
DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {'default': dj_database_url.config()}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
             'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}



STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
STATICFILES_DIRS = ['static/']


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


#django_heroku.settings(locals())


