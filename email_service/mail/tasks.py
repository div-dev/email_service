import logging
from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from .models import emailRecord

# Get an instance of a logger
logger = logging.getLogger('mail')

@shared_task
def send_email_task(email_record_id, iteration=1):
    try:
        email_record = emailRecord.objects.get(id=email_record_id)
        if email_record.is_active:
            send_mail(
                'Test for Email_Service',
                'This is a test Email',
                'divyanshchawla12@gmail.com',
                [email_record.email],
                fail_silently=False,
            )
            logger.debug(f"Email sent to {email_record.email}")

            email_record.last_send_at = timezone.now()
            email_record.save()
            logger.debug(f"EmailRecord updated for {email_record.email}")

            next_interval = 60 * 60
            send_email_task.apply_async(args=[email_record_id, iteration + 1], countdown=next_interval)
            logger.debug(f"Next email scheduled for {email_record.email} in {next_interval / 60} minutes")
    except emailRecord.DoesNotExist:
        logger.error(f"EmailRecord with id {email_record_id} does not exist")
