# subscriptions/management/commands/send_test_email.py

from django.core.mail import send_mail
from django.conf import settings
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Sends a test email to verify email settings'

    def handle(self, *args, **kwargs):
        subject = 'Test Email'
        message = 'This is a test email sent from your Django project12.'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER]  # Send to your own email

        try:
            send_mail(subject, message, from_email, recipient_list)
            self.stdout.write(self.style.SUCCESS('Test email sent successfully!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Failed to send email: {e}'))
