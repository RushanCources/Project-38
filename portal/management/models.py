from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    middle_name = models.TextField(max_length=35, null=True)
    role = models.TextField(max_length=15, default="Ученик")
    group = models.IntegerField(null=True)
    deactivate = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to="avatars", default="avatars/avatar.png")
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self._meta.get_field('username').verbose_name = "Логин"
        self._meta.get_field('password').verbose_name = "Пароль"

    def fullName(self):
        return self.last_name + " " + self.first_name + " " + self.middle_name

class Tokens(models.Model):
    token = models.TextField(max_length=16)
