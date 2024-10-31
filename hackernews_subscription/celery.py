# hackernews_subscription/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hackernews_subscription.settings')
app = Celery('hackernews_subscription')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


# hackernews_subscription/celery.py
from celery.schedules import crontab

app.conf.beat_schedule = {
    'send_top_article_every_day': {
        'task': 'subscriptions.tasks.send_daily_top_article',
        'schedule': crontab(hour=23, minute=21),  # Runs daily at 9 AM
    },
}
