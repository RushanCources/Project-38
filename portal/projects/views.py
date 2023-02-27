from django.http import HttpResponse
from django.shortcuts import render
from management.models import User
from projects.models import Project

def index(request):
    return render(request, "projects/index.html")

def account(request):
    return HttpResponse("Профиль")

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


