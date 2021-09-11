# local.py

from .base import *


DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'OPTIONS': {'timeout': 10,
    }
}
}



STATIC_URL = '/static/'
STATICFILES_DIRS = ['static/']
