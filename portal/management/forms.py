from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)
    username = forms.CharField(label='Логин', min_length=3, max_length=35)
    middle_name = forms.CharField(label='Отчество')
    group = forms.IntegerField(label='Группа', min_value=1, max_value=27)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise ValidationError('Пароли не сходятся!')
        return cd['password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('Логин уже занят!')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Почта уже используется!')
        return email

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'middle_name', 'group', 'email')
