from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=35, unique=False)
    middle_name = models.TextField(max_length=35, null=True)
    role = models.TextField(max_length=15, default="Ученик")
    group = models.IntegerField(null=True)
    email = models.EmailField(max_length=150, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self._meta.get_field('username').verbose_name = "Логин"
        self._meta.get_field('password').verbose_name = "Пароль"

    def fullName(self):
        return self.last_name + " " + self.first_name + " " + self.middle_name
