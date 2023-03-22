from django.db import models
from django.conf import settings


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


class Image(models.Model):
    announcement = models.ForeignKey(Announcement, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='announcement_images', blank=True, null=True)


class File(models.Model):
    announcement = models.ForeignKey(Announcement, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='announcement_files', blank=True, null=True)
