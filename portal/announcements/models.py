from django.db import models
from django.contrib.auth.models import User


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Announcement(TimeStampMixin):
    title = models.CharField(max_length=255)
    body = models.TextField()
    #author = models.ForeignKey(User, on_delete=models.CASCADE)




