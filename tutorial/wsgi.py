import os

from django.core.wsgi import get_wsgi_application

from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)

os.environ["DJANGO_SETTINGS_MODULE"] = "tutorial.settings.production" 

application = get_wsgi_application()

