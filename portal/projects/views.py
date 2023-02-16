from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "projects/index.html")

def account(request):
    return HttpResponse("Профиль")

def create(request):
    return render(request, "projects/create.html")

def postcreate(request):
    student = request.POST.get("student")
    teacher = request.POST.get("teacher")
    name = request.POST.get("name")
    return render(request, "projects/success.html")
