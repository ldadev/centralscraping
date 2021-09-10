#web: python manage.py collectstatic --no-input; gunicorn tutorial.wsgi --log-file - --log-level debug
web: gunicorn tutorial.wsgi

#web: gunicorn --bind 0.0.0.0:$PORT  tutorialdav:app

#web: gunicorn tutorial.wsgi:application --log-file - --log-level debug

#web: python manage.py collectstatic --no-input; gunicorn tutorial.wsgi
