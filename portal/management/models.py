from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def __init__(self, *args, **kwargs):
        super(User,self).__init__(*args, **kwargs)
        self._meta.get_field('username').verbose_name="Логин"
        self._meta.get_field('password').verbose_name="Пароль"


