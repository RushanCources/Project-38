from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    text = "Здесь долен быть проект и возможность им управлять"
    title = "Проект"
    data = {"header" : title, "text" : text}
    return render(request, "index.html", context=data)
