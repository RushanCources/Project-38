from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from .models import Announcement
from datetime import date

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
    is_pinned = request.POST.get("is_pinned")
    de = request.POST.get("date_of_expiring")

    de = de.split("-")

    announcement = Announcement.objects.create(title=str(title), body=str(body), is_pinned=bool(is_pinned), date_of_expiring=date(int(de[0]), int(de[1]), int(de[2])))
    return HttpResponsePermanentRedirect('/announcements')