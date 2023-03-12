from django.shortcuts import redirect, render 
from django.contrib import messages 
from .forms import UserRegistrationForm, UserUpdateForm
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

def token_page(request):
    return render(request, 'registration/token_page.html')    

def admin_menu(request):
    users=User.objects.all()
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST)

        if user_update_form.is_valid():
            user_id = user_update_form.cleaned_data.get("user_id")

            if user_id == -1:
                new_user = user_update_form.save(commit=False)
                new_user.set_password(user_update_form.cleaned_data['password'])
                new_user.save()
            else:    
                user = User.objects.get(id = user_id)
                   
                user.first_name = user_update_form.cleaned_data['first_name']
                user.last_name = user_update_form.cleaned_data['last_name']
                user.middle_name = user_update_form.cleaned_data['middle_name']
                user.username = user_update_form.cleaned_data['username']
                user.group = user_update_form.cleaned_data['group']
                user.role = user_update_form.cleaned_data['role']

                if user.role == 'Администратор':
                    user.is_superuser = True
                    group = 0
                else: 
                    user.is_superuser = False

                user.save() 
            
            return redirect('admin_menu')
    else:
        user_update_form = UserUpdateForm() 

    return render(request, 'admin_menu/admin.html', context={"users" : users, "user_update_form" : user_update_form})

def profile(request):
    users=User.objects.all()
    return render(request, 'profile/profile.html', context={"users" : users})    

