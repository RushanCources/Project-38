from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    pass

class Student(User):
    access = "student"

class Teacher(User):
    access = "teacher"