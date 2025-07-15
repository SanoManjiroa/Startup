web: gunicorn Lison.wsgi --log-file -
#or works good with external database
web: python manage.py migrate && gunicorn Lison.wsgi