from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from .models import Announcement
from datetime import date, datetime
from .decorators import allowed_users
from .models import Tag


def index(request):
    text = "Здесь будет доска обьявлений"
    title = "Доска объявлений"
    data = {"header" : title, "text" : text}
    return render(request, 'dec/dec.html')


#@allowed_users(allowed_roles=['Teacher', 'admin'])
def redactor(request):
    return render(request, "announcements/redactor.html")


#@allowed_users(allowed_roles=['Teacher', 'admin'])
def createannouncement(request):

    if request.method != "POST":
        return HttpResponsePermanentRedirect("/announcements")

    title = request.POST.get("title")
    body = request.POST.get("body")
    is_pinned = request.POST.get("is_pinned")
    de = request.POST.get("date_of_expiring")
    author = request.user
    tags_str = request.POST.get("tags")

    my_tags = []

    tags_list = tags_str.split('\r\n')
    de = de.split("-")

    for name in tags_list:
        tag_exm = Tag(name=name)
        tag_exm.save()
        my_tags.append(tag_exm)

    announcement = Announcement.objects.create(title=str(title), body=str(body), is_pinned=bool(is_pinned), date_of_expiring=date(int(de[0]), int(de[1]), int(de[2])), author=author)
    announcement.tags.add(*my_tags)
    return HttpResponsePermanentRedirect('/announcements')


#@allowed_users(allowed_roles=['Teacher', 'admin'])
def editor(request, id):
    try:
        data = {'announcement': Announcement.objects.get(id=id),
                'date_of_expiring': str(Announcement.objects.get(id=id).date_of_expiring)[:10],
                }

        return render(request, 'announcements/editor.html', context=data)

    except Announcement.DoesNotExist:
        return HttpResponse('Объявление не найдено')


#@allowed_users(allowed_roles=['Teacher', 'admin'])
def editannouncement(request, id):

    try:

        if request.method != "POST":
            return HttpResponsePermanentRedirect('/announcements')

        announcement = Announcement.objects.get(id=id)
        de = request.POST.get("date_of_expiring").split("-")
        date_of_expiring = date(int(de[0]), int(de[1]), int(de[2]))
        is_pinned = request.POST.get("is_pinned")
        tags_str = request.POST.get("tags")
        if is_pinned == '': is_pinned = 0

        my_tags = []

        tags_list = tags_str.split('\r\n')

        for name in tags_list:
            tag_exm = Tag(name=name)
            tag_exm.save()
            my_tags.append(tag_exm)

        announcement.title = request.POST.get("title")
        announcement.body = request.POST.get("body")
        announcement.is_pinned = is_pinned
        announcement.date_of_expiring = date_of_expiring
        announcement.tags.set(my_tags)

        announcement.save()

        return HttpResponsePermanentRedirect('/announcements')

    except Announcement.DoesNotExist:
        HttpResponse('Объявление не найдено')