from django import template
from announcements.models import Notification

register = template.Library()


@register.simple_tag
def unread_notification_count(user):
    return Notification.objects.filter(user=user, read=False).count()
