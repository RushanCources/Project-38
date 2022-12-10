from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    text = "Здесь будет администрирование"
    title = "Панель админа"
    data = {"header" : title, "text" : text}
    return render(request, "index.html", context=data)

def front(r):
    text = "здесь пока что ничего нет"
    title = "Стартовая страница"
    data = {"header" : title, "text" : text}
    return render(r, "index.html", context=data)
