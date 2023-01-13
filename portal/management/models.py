from django.db import models

class User (models.Model):
    username=models.TextField(max_length=30)
    password=models.TextField(max_length=30)
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

class Admin(User):
    def __init__(self, **kwargs):
        super(Admin, self).__init__(**kwargs)
        self.access="admin"

