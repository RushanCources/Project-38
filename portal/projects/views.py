import os

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http.request import HttpRequest

from management.models import User
from projects.models import Project, File
from projects.forms import FileForm


def theme_list(request: HttpRequest):
    return render(request, 'theme_list/theme_list.html')


def index(request: HttpRequest):
    pId = request.GET.get("id", None)
    if pId is None:
        return render(request, "projects/index.html")
    try:
        pId = int(pId)
        project = Project.objects.get(id=pId)
        context = {"name": project.name,
                   "teacher": project.teacher.fullName(),
                   "student": project.student.fullName(),
                   "status": project.get_status(),
                   "description": project.description,
                   "id": pId,
                   }
        return render(request, "projects/project_page.html", context=context)
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


def create(request: HttpRequest):
    if not request.user.is_authenticated:
        return render(request, "NotEnoughPermissions.html")
    if request.user.role != "Ученик":
        return render(request, "NotEnoughPermissions.html")
    teacher_id = request.POST.get("teacher")
    name = request.POST.get("name")
    try:
        teacher = User.objects.get(id=teacher_id)
        subject = request.POST.get("subj")
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


def correct_project(request: HttpRequest):
    if request.method != 'POST':
        return redirect(reverse("projects"))
    if not request.user.is_authenticated:
        return render(request, "NotEnoughPermissions.html")
    project_id = request.POST.get("project", -1)
    if project_id == -1:
        return render(request, "WrongData.html")
    try:
        project_id = int(project_id)
        project = Project.objects.get(id=project_id)
        teacher_id = project.teacher.id
        student_id = project.student.id
        if request.user.id != teacher_id and request.user.id != student_id:
            return render(request, "NotEnoughPermissions.html")
        name = request.POST.get("name", -1)
        description = request.POST.get("description", -1)
        if name != -1:
            project.name = name
            project.save()
        if description != -1:
            project.description = description
            project.save()

        project = Project.objects.get(id=project_id)
        files = File.objects.get(project=project)
        context = {"name": project.name,
                   "teacher": project.teacher.fullName(),
                   "student": project.student.fullName(),
                   "status": project.get_status(),
                   "description": project.description,
                   "id": project_id,
                   'files': files}
        return redirect(reverse("projects") + "?id=" + str(project_id))
    except Project.DoesNotExist:
        return render(request, "WrongData.html")
    except BaseException as e:
        return render(request, "FatalError.html")


# def update_file(request: HttpRequest):
#     if request.method != 'POST':
#         return redirect(reverse("projects"))
#     file = request.FILES.get('file')
#     project = request.POST.get('project')
#     if file is None or project is None:
#         return render(request, "WrongData.html")
#     try:
#         project_files = File.objects.get(project=project, version=1)
#
#
