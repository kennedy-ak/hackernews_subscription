# Procfile

# Django web server
web: gunicorn hackernews_subscription.wsgi --log-file -

# Celery worker
worker: celery -A hackernews_subscription worker --loglevel=info

# Celery beat for scheduling
beat: celery -A hackernews_subscription beat --loglevel=info
