from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User

wrongData = str

def login(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    global wrongData
    if User.objects.filter(username=username).exists():
        person=User.objects.get(username=username)
        if person.password == password and person.access == "admin":
            return HttpResponse(f"""Добро пожаловать, {person.username}""")
        elif person.password != password:
            wrongData = "Не правильно введён пароль"
            return redirect('/management/')
        elif person.access != "admin":
            wrongData = "Вы не администратор"
            return redirect('/management/')
    else:
        wrongData = "Аккаунта с введённым именем не существует"
        return redirect('/management/')


def index(request):
    global wrongData
    tempData = wrongData
    wrongData = str
    return render(request, "login.html", context={"errors": tempData})
    

def front(r):
    text = "здесь пока что ничего нет"
    title = "Стартовая страница"
    data = {"header" : title, "text" : text}
    return render(r, "index.html", context=data)
