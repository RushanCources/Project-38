from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from .models import Announcement
from datetime import date, datetime
from .decorators import allowed_users


def index(request):
    text = "Здесь будет доска обьявлений"
    title = "Доска объявлений"
    data = {"header" : title, "text" : text}
    return render(request, "announcements/index.html", context=data)


@allowed_users(allowed_roles=['Teacher', 'admin'])
def redactor(request):
    return render(request, "announcements/redactor.html")


@allowed_users(allowed_roles=['Teacher', 'admin'])
def createannouncement(request):

    title = request.POST.get("title")
    body = request.POST.get("body")
    is_pinned = request.POST.get("is_pinned")
    de = request.POST.get("date_of_expiring")
    author = request.user

    de = de.split("-")

    announcement = Announcement.objects.create(title=str(title), body=str(body), is_pinned=bool(is_pinned), date_of_expiring=date(int(de[0]), int(de[1]), int(de[2])), author=author)
    return HttpResponsePermanentRedirect('/announcements')


@allowed_users(allowed_roles=['Teacher', 'admin'])
def editor(request, id):
    data = {'announcement': Announcement.objects.get(id=id),
            'date_of_expiring': str(Announcement.objects.get(id=id).date_of_expiring)[:10],
            }

    return render(request, 'announcements/editor.html', context=data)


@allowed_users(allowed_roles=['Teacher', 'admin'])
def editannouncement(request, id):
    announcement = Announcement.objects.get(id=id)
    de = request.POST.get("date_of_expiring").split("-")
    date_of_expiring = date(int(de[0]), int(de[1]), int(de[2]))
    is_pinned = request.POST.get("is_pinned")
    if is_pinned == '': is_pinned = 0

    announcement.title = request.POST.get("title")
    announcement.body = request.POST.get("body")
    announcement.is_pinned = is_pinned
    announcement.date_of_expiring = date_of_expiring

    announcement.save()

    return HttpResponsePermanentRedirect('/announcements')