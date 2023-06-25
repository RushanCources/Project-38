from dataclasses import dataclass

from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http.request import HttpRequest
from django.contrib import messages

from management.models import User
from projects.models import Project, File


def check_what_user_not_have_access(request: HttpRequest, project: Project):  # True если не имеет, False, если имеет
    return request.user.id != project.teacher.id and request.user.id != project.student.id and request.user.role != 'Администратор'


def index(request: HttpRequest):
    project_id = request.GET.get("id", None)
    if project_id is None:
        if request.user.role == 'Ученик':
            projects = Project.objects.filter(student=request.user)
        elif request.user.role == 'Учитель':
            projects = Project.objects.filter(teacher=request.user)

        @dataclass
        class FilePack:
            file: File
            name: str

        @dataclass
        class ProjectPack:
            project: Project
            files: list[FilePack]

        context_projects = []

        for project in projects:
            files = [FilePack(file, file.file.name.split('/')[-1]) for file in File.objects.filter(project=project, version=1)]
            context_projects.append(ProjectPack(project, files))

        return render(request, "projects/index.html", context={'projects': context_projects,
                                                               'has_projects': len(context_projects) > 0})
    try:
        project = Project.objects.get(id=project_id)
        if check_what_user_not_have_access(request, project):
            return render(request, "NotEnoughPermissions.html")
        files = File.objects.filter(project=project, version=1)
        names = [file_obj.file.name.split('/')[-1] for file_obj in files]

        @dataclass
        class FilePack:
            file: File
            name: str

        old_files: list[list[FilePack]] = []
        for file in files:
            old_files.append([])
            if file.previous_file is not None:  # Проверка на наличие предыдущего файла
                prev_file: File = file.previous_file
                file_pack = FilePack(prev_file, prev_file.file.name.split('/')[-1])
                old_files[-1].append(file_pack)
                while prev_file.previous_file is not None:  # Запуск цикла, пока у предыдущего файла есть предыдущий файл
                    prev_file: File = file.previous_file
                    file_pack = FilePack(prev_file, prev_file.file.name.split('/')[-1])
                    old_files[-1].append(file_pack)

        files_packs = []

        @dataclass
        class BranchFilePack:
            file: File
            name: str
            old_files: list[FilePack]

        for i in range(len(files)):
            files_packs.append(BranchFilePack(files[i], names[i], old_files[i]))
        context = {"name": project.name,
                   "teacher": project.teacher.fullName(),
                   "student": project.student.fullName(),
                   "avaurl_of_teacher" : project.teacher.avatar.url,
                   "avaurl_of_student" : project.student.avatar.url,
                   "status": project.get_status(),
                   "description": project.description,
                   "project_id": project_id,
                   'files_packs': files_packs,
                   'files_names': dict(zip([files_pack.name for files_pack in files_packs], [files_pack.file.id for files_pack in files_packs])),
                   }

        return render(request, "projects/project_page.html", context={"project" : context, "users" : User.objects.all(), "files_packs" : files_packs})
    except Project.DoesNotExist:
        return render(request, "WrongData.html")
    except BaseException as e:
        print(e)
        return render(request, "FatalError.html")


def account(request: HttpRequest):
    return HttpResponse("Профиль")


def create_data(request: HttpRequest):
    user1, created = User.objects.get_or_create(username="aaa1", first_name="Надежда", middle_name="Борисовна",
                                                last_name="Тукова", email="a@a.ru", role="Учитель")
    user1.set_password("1")
    user1.save()
    user2, created = User.objects.get_or_create(username="aaa2", first_name="Наталья", middle_name="Львовна",
                                                last_name="Попова", email="a@a.ru",
                                                role="Учитель")
    user2.set_password("1")
    user2.save()
    user3, created = User.objects.get_or_create(username="aaa3", first_name="Алексей", middle_name="Романович",
                                                last_name="Дмитриев", email="a@a.ru",
                                                role="Ученик")
    user3.set_password("1")
    user3.save()
    user4, created = User.objects.get_or_create(username='d1ffy', last_name='Кокорин', first_name='Петр', middle_name='Алексеевич',
                                                email='helpersteam96@inbox.ru', role='Администратор')
    user4.set_password("1")
    user4.save()
    user5, created = User.objects.get_or_create(username='Cbytl', last_name='Кабанин', first_name='Денис', middle_name='Андреевич',
                                                email='email@email.ru', role='Администратор')
    user5.set_password("555555")
    user5.save()
    project = Project.objects.create(name="Проект1", teacher=user1, student=user3)
    project.set_subject("Математика")
    project.save()
    return HttpResponse("Всё ок")


def send_create_form(request: HttpRequest):
    if request.user.is_authenticated:
        if request.user.role == "Ученик":
            teachers = User.objects.filter(role="Учитель")
            data = {"teachers": teachers}
            return render(request, "projects/create.html", data)
    return render(request, "NotEnoughPermissions.html")


def check_post_request(*need_values):
    def decorator(func):
        def wrapper(request):
            if request.method != 'POST':
                return redirect(reverse("projects"))
            if not request.user.is_authenticated:
                messages.error(request, 'У вас нет прав для совершения этого действия')
                return render(request, "projects/create.html")

            for value in need_values:
                request_value = request.POST.get(value, '')
                if request_value == '':
                    messages.error(request, 'Неверно введённые данные')
                    return render(request, "projects/create.html")
            return func(request)
        return wrapper
    return decorator


@check_post_request('teacher', 'name', "subject")
def create(request: HttpRequest):
    teacher_id = request.POST.get("teacher")
    subject = request.POST.get("subject")
    name = request.POST.get("name")
    is_another_teacher = request.POST.get('teacher-checkbox')
    print(is_another_teacher)
    try:
        if is_another_teacher == 'on':
            another_teacher = request.POST.get("new-teacher")
            last_user = User.objects.last()
            if last_user is None:
                new_id = 1
            else:
                new_id = last_user.pk + 1
            teacher: User = User.objects.create_user(username=new_id, first_name=another_teacher.split()[0],
                                                     last_name=another_teacher.split()[1], middle_name=another_teacher.split()[2],
                                                     role='Учитель', id=new_id)
            teacher.set_password(User.objects.make_random_password(30))
            teacher.save()
        else:
            teacher = User.objects.get(id=teacher_id)
        if teacher.role != "Учитель":
            return render(request, "WrongData.html")
        project = Project.objects.create(name=name, teacher=teacher, student=request.user)
        project.set_subject(subject)
        project.set_status("send request")
        project.save()
        files = request.FILES.getlist('files')
        for file in files:
            file_object = File.objects.create(project=project, file=file, version=1)
            file_object.save()
        return render(request, "projects/success.html")
    except User.DoesNotExist:
        return render(request, "WrongData.html")
    except BaseException as e:
        return render(request, "FatalError.html")


@check_post_request('project')
def correct_project(request: HttpRequest):
    project_id = request.POST.get("project")
    print(project_id)
    try:
        project_id = project_id
        project = Project.objects.get(id=project_id)
        if check_what_user_not_have_access(request, project):
            return render(request, "NotEnoughPermissions.html")
        name = request.POST.get("name", -1)
        description = request.POST.get("description", -1)
        if name != -1:
            project.name = name
            project.save()
        if description != -1:
            project.description = description
            project.save()
        return redirect(f"{reverse('projects')}?id={project_id}")
    except Project.DoesNotExist:
        return render(request, "WrongData.html")
    except BaseException as e:
        return render(request, "FatalError.html")


@check_post_request('file_id')
def update_file(request: HttpRequest):
    file_id = request.POST.get('file_id')
    file = request.FILES.get('file')
    try:
        file_object: File = File.objects.get(id=file_id)
        project = file_object.project
        if check_what_user_not_have_access(request, project):
            return render(request, "NotEnoughPermissions.html")
        file_object.update_file(file)
        return redirect(f"{reverse('projects')}?id={project.id}")
    except File.DoesNotExist:
        return render(request, "WrongData.html")
    except Project.DoesNotExist:
        return render(request, "WrongData.html")
    except BaseException as e:
        print(e)
        return render(request, "FatalError.html")


@check_post_request('file_id')
def delete_file(request: HttpRequest):
    file_id = request.POST.get('file_id')
    try:
        file = File.objects.get(id=file_id)
        project = file.project
        if check_what_user_not_have_access(request, project):
            return render(request, "NotEnoughPermissions.html")
        file.move_to_trash()
        return redirect(f"{reverse('projects')}?id={project.id}")
    except File.DoesNotExist:
        return render(request, "WrongData.html")
    except BaseException as e:
        return render(request, "FatalError.html")


def download_file(request: HttpRequest):
    file_id = request.GET.get('file_id')
    if file_id is None:
        return render(request, "WrongData.html")
    try:
        file_object = File.objects.get(id=file_id)
        if check_what_user_not_have_access(request, file_object.project):
            return render(request, "NotEnoughPermissions.html")
        filepath = file_object.file.path
        return FileResponse(open(filepath, 'rb'), as_attachment=True)
    except File.DoesNotExist:
        return render(request, "WrongData.html")
    except BaseException as e:
        return render(request, "FatalError.html")


@check_post_request("project_id")
def upload_file(request: HttpRequest):
    project_id = request.POST.get("project_id")
    file = request.FILES.get("file")
    try:
        project = Project.objects.get(id=project_id)
        if check_what_user_not_have_access(request, project):
            return render(request, "NotEnoughPermissions.html")
        print(file)
        file_object = File.objects.create(project=project, file=file, version=1)
        file_object.save()
        return redirect(f"{reverse('projects')}?id={project.id}")
    except Project.DoesNotExist:
        return render(request, "WrongData.html")
    except BaseException as e:
        print(e)
        return render(request, "FatalError.html")


def get_trash(request: HttpRequest):
    project_id = request.GET.get('project_id')
    if project_id is None:
        return render(request, "WrongData.html")
    try:
        project = Project.objects.get(id=project_id)
        files = File.objects.filter(project=project, version=-1)
        names = [file.file.name.split('/')[-1] for file in files]
        files_and_names = zip(files, names)
        context = {"files": files_and_names}
        return render(request, "projects/trash.html", context=context)
    except Project.DoesNotExist:
        return render(request, "WrongData.html")
    except BaseException as e:
        return render(request, "FatalError.html")


@check_post_request('file_id')
def restore_file(request: HttpRequest):
    file_id = request.POST.get("file_id")
    try:
        file = File.objects.get(id=file_id)
        project = file.project
        if check_what_user_not_have_access(request, project):
            return render(request, "NotEnoughPermissions.html")
        file.restore()
        return redirect(f"{reverse('projects')}?id={project.id}")
    except File.DoesNotExist:
        return render(request, "WrongData.html")
    except BaseException as e:
        return render(request, "FatalError.html")


@check_post_request('comment', "file_id")
def set_comment(request: HttpRequest):
    comment = request.POST.get("comment")
    file_id = request.POST.get("file_id")
    try:
        file = File.objects.get(id=file_id)
        project = file.project
        if check_what_user_not_have_access(request, project):
            return render(request, "NotEnoughPermissions.html")
        file.comment = comment
        file.save()
        return redirect(f"{reverse('projects')}?id={project.id}")
    except File.DoesNotExist:
        return render(request, "WrongData.html")
    except BaseException as e:
        return render(request, "FatalError.html")


@check_post_request('project_id')
def approve_project(request: HttpRequest):
    project_id = request.POST.get('project_id')
    try:
        project = Project.objects.get(id=project_id)
        project.set_status('on work')
        return redirect(f"{reverse('projects')}?id={project.id}")
    except Project.DoesNotExist:
        return render(request, "WrongData.html")
    except BaseException as e:
        return render(request, "FatalError.html")


@check_post_request('project_id')
def close_project(request: HttpRequest):
    project_id = request.POST.get('project_id')
    try:
        project = Project.objects.get(id=project_id)
        project.set_status('done')
        return redirect(f"{reverse('projects')}?id={project.id}")
    except Project.DoesNotExist:
        return render(request, "WrongData.html")
    except BaseException as e:
        return render(request, "FatalError.html")
