from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "projects/index.html")

def account(request):
    return HttpResponse("Профиль")

def create(request):
    if request.user.is_authenticated:
        if request.user.role == "Ученик":
            return render(request, "projects/create.html")
    return render(request, "NotEnoughPermissions.html")

def postcreate(request):
    if not request.user.is_authenticated:
        return render(request, "NotEnoughPermissions.html")
    if request.user.role != "Ученик":
        return render(request, "NotEnoughPermissions.html")
    teacher = request.POST.get("teacher")
    name = request.POST.get("name")
    return render(request, "projects/success.html")
