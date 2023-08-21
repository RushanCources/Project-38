from django.db import models

class Theme(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    type = models.CharField(max_length=10)
    subjects = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    descript = models.CharField(max_length=2000)
    subject_color = models.CharField(max_length=20, null=True)
    class_of_tag = models.CharField(max_length=100, null=True)

class Subject(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=20)