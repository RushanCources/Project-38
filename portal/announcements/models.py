from django.db import models
from django.conf import settings


class Tag(models.Model):
    name = models.CharField(max_length=50)


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
    tags = models.ManyToManyField(Tag)
    image_urls = models.TextField(blank=True)


