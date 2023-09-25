from django.db import models
from django.conf import settings
from django.contrib.staticfiles import finders


class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    announcement_id = models.IntegerField(null=True)


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Announcement(TimeStampMixin):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_pinned = models.BooleanField(default=False)
    date_of_expiring = models.DateTimeField(null=True)
    image_url = models.FilePathField(null=True, path=finders.find("img/announcements/covers"))


class File(models.Model):
    announcement = models.ForeignKey(Announcement, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='announcement_files', blank=True, null=True)
