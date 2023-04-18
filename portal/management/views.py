from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm
from .models import User, Tokens


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            messages.success(request, 'Аккаунт успешно создан')
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
    users = User.objects.all()
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST)

        if user_update_form.is_valid():
            user_id = user_update_form.cleaned_data.get("user_id")

            if user_id == -1:
                new_user = user_update_form.save(commit=False)
                new_user.set_password(user_update_form.cleaned_data['password'])
                new_user.save()
            else:
                user = User.objects.get(id=user_id)
                first_name = user_update_form.cleaned_data.get("first_name")
                last_name = user_update_form.cleaned_data.get("last_name")
                middle_name = user_update_form.cleaned_data.get("middle_name")
                username = user_update_form.cleaned_data.get("username")
                group = user_update_form.cleaned_data.get("group")
                role = user_update_form.cleaned_data.get("role")
                # password = user_update_form.cleaned_data.get("password")

                if role == 'Администратор':
                    user.is_superuser = True
                    group = 0
                else:
                    user.is_superuser = False

                user.first_name = first_name
                user.last_name = last_name
                user.middle_name = middle_name
                user.username = username
                user.group = group
                user.role = role
                # user.password = password
                # Изначально пароль выводится не дешифрованным, шакальным короче и таким же он передаётся  сюда, как проблему исправите, можно будет и пароль изменять
                user.save()  # Сохраняется криво, хз в чём проблема, но работает через раз

            return redirect('admin_menu')
    else:
        user_update_form = UserUpdateForm()

    return render(request, 'admin_menu/admin.html', context={"users": users, "user_update_form": user_update_form})


def profile(request):
    users = User.objects.all()
    return render(request, 'profile/profile.html', context={"users": users})
