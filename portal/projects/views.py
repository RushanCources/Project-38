import os

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse
from management.models import User
from projects.models import Project

def index(request):
    pId = request.GET.get("id", None)
    if pId is None:
        return render(request, "projects/index.html")
    try:
        pId = int(pId)
        project = Project.objects.get(id=pId)
        context = { "name" : project.name,
                    "teacher" : project.teacher.fullName(),
                    "student" : project.student.fullName(),
                    "status" : project.getStatus(),
                    "description" : project.description,
                    "id" : pId}
        return render(request, "projects/project_page.html", context=context)
    except Project.DoesNotExist:
        return render(request, "WrongData.html")
    except BaseException as e:
        return render(request, "FatalError.html")


def account(request):
    return HttpResponse("Профиль")

def jslibs(request):
    file_location=""
    filename = ""
    if request.path == reverse("select2"):
        file_location = os.getcwd()[0:-7]+r"\Assets LTE\plugins\select2\js\select2.full.min.js"
        filename = "select2.full.min.js"
    elif request.path == reverse("jquery"):
        file_location = os.getcwd()[0:-7]+r"\Assets LTE\plugins\jquery\jquery.min.js"
        filename = "jquery.min.js"
    try:
        with open(file_location, 'r', encoding='utf-8') as f:
            file_data = f.read()

        # sending response
        response = HttpResponse(file_data, content_type='text/javascript')
        response['Content-Disposition'] = 'attachment; filename="'+filename+'"'

    except IOError:
        # handle file not exist case here
        response = HttpResponseNotFound('<h1>File not exist</h1>')
    return response

def csslibs(request):
    file_location=""
    filename=""
    if request.path == reverse("select2css"):
        file_location = os.getcwd()[0:-7]+r"\Assets LTE\plugins\select2\css\select2.min.css"
        filename = "select2.min.css"
    try:
        with open(file_location, 'r', encoding='utf-8') as f:
            file_data = f.read()

        # sending response
        response = HttpResponse(file_data, content_type='text/css')
        response['Content-Disposition'] = 'attachment; filename="'+filename+'"'

    except IOError:
        # handle file not exist case here
        response = HttpResponseNotFound('<h1>File not exist</h1>')
    return response

def create(request):
    if request.user.is_authenticated:
        if request.user.role == "Ученик":
            teachers = User.objects.filter(role="Учитель")
            data = {"teachers" : teachers}
            return render(request, "projects/create.html", data)
    return render(request, "NotEnoughPermissions.html")

def postcreate(request):
    if not request.user.is_authenticated:
        return render(request, "NotEnoughPermissions.html")
    if request.user.role != "Ученик":
        return render(request, "NotEnoughPermissions.html")
    teacherId = request.POST.get("teacher")
    name = request.POST.get("name")
    try:
        teacher = User.objects.get(id = teacherId)
        if teacher.role != "Учитель":
            return render(request, "WrongData.html")
        project = Project.objects.create(name = name, teacher = teacher, student = request.user)
        project.setStatus("send request")
        return render(request, "projects/success.html")
    except User.DoesNotExist:
       return render(request, "WrongData.html")
    except BaseException:
        return render(request, "FatalError.html")

def correctProject(request):
    if not request.user.is_authenticated:
        return render(request, "NotEnoughPermissions.html")
    pId = request.POST.get("project", -1)
    print(pId)
    if pId == -1:
        return render(request, "WrongData.html")
    try:
        pId = int(pId)
        project = Project.objects.get(id = pId)
        teacherId = project.teacher.id
        studentId = project.student.id
        if request.user.id != teacherId and request.user.id != studentId:
            return render(request, "NotEnoughPermissions.html")
        name = request.POST.get("name", -1)
        description = request.POST.get("description", -1)
        if name == -1 and description == -1:
            return render(request, "WrongData.html")
        if name != -1:
            project.name = name
            project.save()
        elif description != -1:
            project.description = description
            project.save()
        project = Project.objects.get(id=pId)
        context = {"name": project.name,
                   "teacher": project.teacher.fullName(),
                   "student": project.student.fullName(),
                   "status": project.getStatus(),
                   "description": project.description,
                   "id": pId}
        return redirect(reverse("projects")+"?id="+str(pId))
    except Project.DoesNotExist:
        return render(request, "WrongData.html")
    except BaseException as e:
        print(e)
        return render(request, "FatalError.html")


