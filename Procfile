#web: gunicorn tutorial.wsgi --log-file - 

#web: gunicorn --bind 0.0.0.0:$PORT  tutorialdav:app

web: gunicorn django_project.wsgi:application --log-file - --log-level debug
