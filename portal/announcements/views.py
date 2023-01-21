from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from .models import Announcement

def index(request):
    text = "Здесь будет доска обьявлений"
    title = "Доска объявлений"
    data = {"header" : title, "text" : text}
    return render(request, "index.html", context=data)


def redactor(request):
    return render(request, "announcements/redactor.html")


def createannouncement(request):
    title = request.POST.get("title")
    body = request.POST.get("body")
    announcement = Announcement.objects.create(title=str(title), body=str(body))
    return HttpResponsePermanentRedirect('/announcements')