from django.shortcuts import redirect, render 
from django.contrib import messages 
from .forms import UserRegistrationForm
from .models import User, Tokens
 
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
    if request.method == "POST":
        token = request.POST.get("token")
        if Tokens.objects.filter(token=token).exists():
            temp_token = Tokens.objects.get(token=token).delete()
            return redirect('register')
        else:
            messages.error(request, 'Неправильный токен!')
    
    return render(request, 'registration/token_page.html')

def admin_menu(request):
    users=User.objects.all()
    if request.method == "POST":
        user_id = request.POST.get('user_id_edit')
        first_name = request.POST.get('name_input')
        last_name = request.POST.get('surname_input')
        middle_name = request.POST.get('patronymic_input')
        username = request.POST.get('login_input')
        group = request.POST.get('group_input')
        role = request.POST.get('role')

        if user_id == -1:
            new_user = User.objects.create(username = username, first_name = first_name, last_name = last_name, middle_name = middle_name, group = group, role = role)
            new_user.set_password(request.POST.get('password'))
            new_user.save()
        
        else:
            user = User.objects.get(id=user_id)
            user.first_name = first_name
            user.last_name = last_name
            user.middle_name = middle_name
            user.username = username
            user.group = group
            user.role = role
            if role == "Администратор":
                user.group = 0
                user.is_superuser = True
            elif role == "Учитель":
                user.group = 0
            else:
                user.is_superuser = False

            user.save()
        
        return redirect('admin_menu')
    

    return render(request, 'admin_menu/admin.html', context={"users" : users})

def profile(request):
    users=User.objects.all()
    return render(request, 'profile/profile.html', context={"users" : users})    

