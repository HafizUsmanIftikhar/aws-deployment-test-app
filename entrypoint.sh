#!/bin/sh

python manage.py migrate --no-input
# collect all static files to the root directory
python manage.py collectstatic --no-input

# start the gunicorn worker process at the defined port
gunicorn mysite.wsgi:application --bind 0.0.0.0:8000 &
wait
