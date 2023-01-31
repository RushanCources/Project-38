from liceum38.celery import app
from datetime import timedelta
from django.utils import timezone
from .models import Announcement
from celery import shared_task


@shared_task
def delete_expired_values():
    announcements = Announcement.objects.all()
    for announcement in announcements:
        dt = announcement.date_of_expiring.date()
        if dt == timezone.now().date():
            announcement.delete()
