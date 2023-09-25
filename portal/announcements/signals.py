from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import Announcement, Notification


@receiver(post_save, sender=Announcement)
def create_notifications_for_new_announcement(sender, instance, **kwargs):
    users = get_user_model().objects.all()

    for user in users:
        Notification.objects.create(user=user, announcement_id=instance.id)
