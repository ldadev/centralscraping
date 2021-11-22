# local.py

from .base import *


DEBUG = True
ALLOWED_HOSTS = ['*']

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'OPTIONS': {'timeout': 10,
    }
}
}

"""


DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'central',

        'USER': 'dadev',

        'PASSWORD': '1580',

        'HOST': 'localhost',

        'PORT': '',

    }

}

STATIC_URL = '/static/'
STATICFILES_DIRS = ['static/']
