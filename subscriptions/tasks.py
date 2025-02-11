# subscriptions/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from .models import Subscriber
from .utils import get_top_article
from django.conf import settings


# def send_daily_top_article():
#     print("Sending top article email to subscribers...")
#     subject = "Top Hacker News Article-by Kennedy"
#     article_title, article_link = get_top_article()
#     message = f"Today's top article: {article_title}\nRead more at: {article_link}"
    
#     subscribers = Subscriber.objects.values_list('email', flat=True)
#     for email in subscribers:
#         send_mail(subject, message, settings.EMAIL_HOST_USER, [email])

@shared_task
def send_daily_top_article():
    print("Sending top article email to subscribers...")
    subject = "Top Hacker News Article-by Kennedy"
    article_title, article_link = get_top_article()
    message = f"Today's Top Tech article: {article_title}\nRead more at: {article_link}"

    subscribers = Subscriber.objects.values_list('email', 'name')
    for email, name in subscribers:
        personalized_message = f"Hi {name},\n\n{message}"
        send_mail(subject, personalized_message, settings.EMAIL_HOST_USER, [email])
