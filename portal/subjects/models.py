from django.db import models

class Theme(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    subject = models.CharField(max_length=20)
    status = models.CharField(max_length=20)  # Статус темы [Свободна], [Занята], [Прошлых лет]
    descript = models.CharField(max_length=2000)