from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image

class User(AbstractUser):
    middle_name = models.TextField(max_length=35, default="Нет")
    role = models.TextField(max_length=15, default="Ученик")
    group = models.IntegerField(null=True)
    deactivate = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to="avatars", default="avatars/avatar.png")
    is_view_window = models.BooleanField(default=False)
    full_Name = models.TextField(max_length=100, null=True)
    is_other_teacher = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self._meta.get_field('username').verbose_name = "Логин"
        self._meta.get_field('password').verbose_name = "Пароль"
    
    def set_full_name(self):
        self.full_Name = self.last_name + self.first_name + self.middle_name
    
    def get_full_name(self) -> str:
        return self.last_name+' '+self.first_name+' '+self.middle_name;

    def save_photo(self, *args, **kwargs):
        super().save()
        img = Image.open(self.avatar.path)
        width, height = img.size  # Get dimensions

        if width > 300 and height > 300:
            # keep ratio but shrink down
            img.thumbnail((width, height))

        # check which one is smaller
        if height < width:
            # make square by cutting off equal amounts left and right
            left = (width - height) / 2
            right = (width + height) / 2
            top = 0
            bottom = height
            img = img.crop((left, top, right, bottom))

        elif width < height:
            # make square by cutting off bottom
            left = 0
            right = width
            top = 0
            bottom = width
            img = img.crop((left, top, right, bottom))

        if width > 300 and height > 300:
            img.thumbnail((300, 300))

        img.save(self.avatar.path)

    def getPName(self):
        return self.last_name + " " + self.first_name[0] + "." + self.middle_name[0]

class Tokens(models.Model):
    token = models.TextField(max_length=16)
