web: gunicorn --pythonpath critical_critiques critical_critiques.wsgi
worker: python critical_critiques/manage.py celery worker
