from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    text = "Здесь будет доска обьявлений"
    title = "Доска объявлений"
    data = {"header" : title, "text" : text}
    return render(request, "index.html", context=data)