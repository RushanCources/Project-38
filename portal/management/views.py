import string
import random
from dataclasses import dataclass, field

from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render 
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import User, Tokens
from projects.models import Project
 
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            messages.success(request, 'Аккаунт успешно создан')
            authenticate_user = authenticate(request, username=new_user.username, password=new_user.password)
            login(request, authenticate_user)
            return redirect('profile')
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
    filter_users = User.objects.filter(deactivate=0)
    if request.method == "POST":
        user_id = request.POST.get('user_id_edit')
        user_id_delete = request.POST.get('user_id_delete')
        token_value = request.POST.get('token_value')
        first_name = request.POST.get('name_input')
        last_name = request.POST.get('surname_input')
        middle_name = request.POST.get('patronymic_input')
        username = request.POST.get('login_input')
        group = request.POST.get('group_input')
        role = request.POST.get('role')
        email = request.POST.get('email_input')
        search_names = request.POST.get('search_names')

        if request.POST.get('delete_butt'):
            user = User.objects.get(id=user_id_delete).delete()
            return redirect('admin_menu')

        if request.POST.get('deactivate_butt'):
            user = User.objects.get(id=user_id_delete)
            user.deactivate = True
            user.save()
            return redirect('admin_menu')

        if request.POST.get('accept_token'):
            last_token = Tokens.objects.last()
            if last_token is None:
                new_id = 1
            else:
                new_id = last_token.pk + 1
            for i in range(int(token_value)):
                token = Tokens.objects.create(token=generate_alphanum_random_string(16), id=new_id + i)
                token.save()
            return redirect('admin_menu')
        
        if request.POST.get('search_butt'):
            filter_users = User.objects.filter()
            return redirect('admin_menu')

        if user_id == "-1":
            last_user = User.objects.last()
            if last_user is None:
                new_id = 1
            else:
                new_id = last_user.pk + 1
            new_user = User.objects.create(username=username, first_name=first_name, last_name=last_name,
                                           middle_name=middle_name, group=group, role=role, email=email, password=0,
                                           id=new_id)
            new_user.set_password(request.POST.get('password_input'))
            new_user.save()
            return redirect('admin_menu')

        else:
            user = User.objects.get(id=user_id)
            user.first_name = first_name
            user.last_name = last_name
            user.middle_name = middle_name
            user.username = username
            user.group = group
            user.role = role
            user.email = email
            if role == "Администратор":
                user.group = 0
                user.is_superuser = True
            elif role == "Учитель":
                user.group = 0
            else:
                user.is_superuser = False

            user.save()

            return redirect('admin_menu')

    return render(request, 'admin_menu/admin.html', context={"users": filter_users})


def profile(request):
    @dataclass
    class ProjectsPack:
        project: Project
        student_p_name: str = field(init=False)
        teacher_p_name: str = field(init=False)

        def __post_init__(self):
            self.student_p_name = self.project.student.getPName()
            self.teacher_p_name = self.project.teacher.getPName()

    if request.user.role == 'Ученик':
        open_projects_st: list[Project] = Project.objects.filter(student = request.user, _status = "on work")
        close_projects_st: list[Project] = Project.objects.filter(student_id = request.user, _status = "done")
        request_projects_st: list[Project] = Project.objects.filter(student=request.user, _status = "send request")
        open_projects_packs = [ProjectsPack(project) for project in open_projects_st]
        close_projects_packs = [ProjectsPack(project) for project in close_projects_st]
        request_projects_packs = [ProjectsPack(project) for project in request_projects_st]
    else:

        open_projects_T = Project.objects.filter(teacher=request.user, _status = "on work")
        close_projects_T = Project.objects.filter(teacher=request.user, _status = "done")
        request_projects_T = Project.objects.filter(teacher=request.user, _status = "send request")
        open_projects_packs = [ProjectsPack(project) for project in open_projects_T]
        close_projects_packs = [ProjectsPack(project) for project in close_projects_T]
        request_projects_packs = [ProjectsPack(project) for project in request_projects_T]
    user_full = request.user.getPName()


    if request.method == "POST":
        new_password = request.POST.get('new_password')
        old_password = request.POST.get('old_password')
        repeat_password = request.POST.get('repeat_password')
        username = request.POST.get('username_inp')
        email = request.POST.get('email_inp')
        first_name = request.POST.get('first_name_inp')
        middle_name = request.POST.get('middle_name_inp')
        last_name = request.POST.get('last_name_inp')
        new_avatar = request.FILES['avatar_inp']

        if request.POST.get('submit_changes'):
            request.user.email = email
            request.user.first_name = first_name
            request.user.middle_name = middle_name
            request.user.last_name = last_name
            request.user.username = username
            request.user.save()

            if request.user.check_password(old_password):
                if new_password == repeat_password:
                    request.user.set_password(new_password)
                    request.user.save()
                    new_user = authenticate(request, username=username, password=new_password)
                    login(request, new_user)
                    return redirect('profile')


        if request.POST.get('avatar_submit') and request.FILES:
            request.user.avatar = new_avatar
            request.user.save()
            return redirect('profile')

    context = {"open_projects_packs": open_projects_packs,
               "close_projects_packs": close_projects_packs,
               "user_full": user_full,
               "request_projects_packs": request_projects_packs,
               "request_projects_length": len(request_projects_packs)}
    return render(request, 'profile/profile.html', context)


def generate_alphanum_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    return rand_string
