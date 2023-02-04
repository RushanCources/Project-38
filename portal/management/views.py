from django.shortcuts import redirect, render 
from django.contrib import messages 
from .forms import UserRegistrationForm
from .models import User
 
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            messages.success(request,'Аккаунт успешно создан')
            return redirect('register')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})

def admin_menu(request):
    users=User.objects.all()
    return render(request, 'admin_menu/admin.html', context={"users" : users})

