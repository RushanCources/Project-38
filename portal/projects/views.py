import os

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse

from management.models import User
from projects.models import Project

def index(request):
    return render(request, "projects/index.html")

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
    elif request.path == reverse("selec2css"):
        file_location = os.getcwd()[0:-7]+r"\Assets LTE\plugins\select2\css\select2.min.css"
        filename = "select2.min.css"
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
    if request.path == reverse("selec2css"):
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
    except BaseException:
        return render(request, "FatalError.html")


