from django.db import models

# Create your models here.
class User (models.Model):
    name=models.CharField(max_length=30)
    lastName=models.CharField(max_length=30)
    fatherName=models.CharField(max_length=30)
    access=models.CharField(max_length=30)

class Student(User):
    def __init__(self, **kwargs):
        super(student, self).__init__(**kwargs)
        self.access="student"

class Teacher(User):
    def __init__(self, **kwargs):
        super(Teacher, self).__init__(**kwargs)
        self.access="teacher"
