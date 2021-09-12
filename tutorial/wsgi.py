import os
from django.core.wsgi import get_wsgi_application


os.environ["DJANGO_SETTINGS_MODULE"] = "tutorial.settings.production"
#os.environ["DJANGO_SETTINGS_MODULE"] = "tutorial.settings.development" 


application = get_wsgi_application()
