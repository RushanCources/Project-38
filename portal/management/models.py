from django.contrib.auth.models import AbstractUser

class User(AbstractUser):


class Student(User):
    access = "student"

class Teacher(User):
    access = "teacher"