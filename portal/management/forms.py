from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth import get_user_model

User=get_user_model()

class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Логин', min_length=5, max_length=150) 
    email = forms.EmailField(label='Адрес электронной почты') 
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput) 
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Имя', min_length=1, max_length=40)
    last_name = forms.CharField(label='Фамилия', min_length=1, max_length=40)

 
    def username_clean(self): 
        username = self.cleaned_data['username'].lower() 
        new = User.objects.filter(username = username)
        if new.count(): 
            messages.error("Данный логин уже занят") 
        return username 
 
    def email_clean(self): 
        email = self.cleaned_data['email'].lower() 
        new = User.objects.filter(email=email) 
        if new.count(): 
            messages.error("Аккаунт с такой электронной почтой уже создан") 
        return email 
 
    def clean_password2(self): 
        password1 = self.cleaned_data['password1'] 
        password2 = self.cleaned_data['password2'] 
 
        if password1 and password2 and password1 != password2: 
            messages.error("Пароли не сходяться") 
        return password2 

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        
        return last_name
 
    def save(self, commit = True): 
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1'],
            first_name = self.cleaned_data['first_name'],
            last_name = self.cleaned_data['last_name']
        ) 
        return user 