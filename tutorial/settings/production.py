# .production.py

from .base import *
import dj_database_url
import django_heroku


#DEBUG =  os.environ.get('DJANGO_DEBUG', default='False')
DEBUG = os.environ['DEBUG']
ALLOWED_HOSTS = ['tutorialdav.herokuapp.com']

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'dd8p2lpah7864b',

        'USER': 'qxxqgbbbfktwgm',

        'PASSWORD': '81d1a7e14257eb09c9dacb171b065603e31e0fc925068d25abcf13093c73fb15',

        'HOST': 'ec2-44-199-19-138.compute-1.amazonaws.com',

        'PORT': '',

    }

}

DATABASES = {'default': dj_database_url.config()}




STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
STATICFILES_DIRS = ['static/']


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


django_heroku.settings(locals())


