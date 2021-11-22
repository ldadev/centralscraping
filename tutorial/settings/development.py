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

"""
DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'central',

        'USER': 'dadev',

        'PASSWORD': '1580',

        'HOST': 'localhost',

        'PORT': '5432',

    }

}

"""

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

STATIC_URL = '/static/'
STATICFILES_DIRS = ['static/']
