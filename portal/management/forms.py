from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User=get_user_model()

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)
    username= forms.CharField(label='Имя пользователя', min_length=3, max_length=35)

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не сходятся')
        return cd['password2']
 
    def username_clean(self): 
        username = self.cleaned_data['username']
        if User.objects.filter(username = username).exists(): 
            raise forms.ValidationError('Аккаунт с такими логином уже существует')
        return username 
 
    def email_clean(self): 
        email = self.cleaned_data['email']
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError("Аккаунт с такой электронной почтой уже создан") 
        return email 