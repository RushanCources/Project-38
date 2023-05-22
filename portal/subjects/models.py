from django.db import models

class Theme(models.Model):
    Name = models.CharField(max_length=100)
    Author = models.CharField(max_length=30)
    Type = models.CharField(max_length=10)
    Subject = models.CharField(max_length=20)
    Status = models.CharField(max_length=20)
    Descript = models.CharField(max_length=2000)
    Class_of_subject = models.CharField(max_length=100)
    Class_of_tag = models.CharField(max_length=100, null=True)
