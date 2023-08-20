from django.db import models

class Theme(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    type = models.CharField(max_length=10)
    subject = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    descript = models.CharField(max_length=2000)
    class_of_subject = models.CharField(max_length=100)
    class_of_tag = models.CharField(max_length=100, null=True)
