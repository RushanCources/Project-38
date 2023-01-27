from django.contrib.auth import forms 
from django.shortcuts import redirect, render 
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm 
from .forms import CustomUserCreationForm
 
def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Аккаунт успешно создан')
            return redirect('register')

    else:
        f = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': f})

