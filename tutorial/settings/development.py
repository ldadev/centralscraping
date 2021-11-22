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

        'NAME': 'dbnvr8hpfqomqu',

        'USER': 'ejosjcofprbnde',

        'PASSWORD': '195b50bc50224605aa3a497f73f2daebc25f4cf13149c772fca96d13fea77e16',

        'HOST': 'ec2-107-22-18-26.compute-1.amazonaws.com',

        'PORT': '',

    }

}

STATIC_URL = '/static/'
STATICFILES_DIRS = ['static/']
