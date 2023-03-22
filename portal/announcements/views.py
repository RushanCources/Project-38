from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from .models import Announcement
from datetime import date
from .decorators import allowed_users
from .models import Image, File


def index(request):

    group = None
    superuser = False

    if request.user.groups.exists():
        group = request.user.groups.all()[0].name
    if group in ['Teacher', 'admin']:
        superuser = True

    data = {'superuser': superuser}

    return render(request, 'dec/dec.html', context=data)


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
    images = request.FILES.getlist('images')
    files = request.FILES.getlist('files')

    de = de.split("-")

    announcement = Announcement.objects.create(title=str(title), body=str(body), is_pinned=bool(is_pinned), date_of_expiring=date(int(de[0]), int(de[1]), int(de[2])), author=author)

    for image in images:
        Image.objects.create(announcement=announcement, image=image)

    for file in files:
        File.objects.create(announcement=announcement, file=file)

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
        if is_pinned == '': is_pinned = 0
        images_to_delete = request.POST.getlist('images_to_delete')
        images_to_add = request.FILES.getlist('images_to_add')
        files_to_add = request.FILES.getlist('files_to_add')
        files_to_delete = request.POST.getlist('files_to_delete')

        for image_id in images_to_delete:
            image = Image.objects.get(pk=image_id)
            image.image.delete()
            image.delete()

        for image in images_to_add:
            Image.objects.create(announcement=announcement, image=image)

        for file_id in files_to_delete:
            file = File.objects.get(pk=file_id)
            file.file.delete()
            file.delete()

        for file in files_to_add:
            File.objects.create(announcement=announcement, file=file)

        announcement.title = request.POST.get("title")
        announcement.body = request.POST.get("body")
        announcement.is_pinned = is_pinned
        announcement.date_of_expiring = date_of_expiring

        announcement.save()

        return HttpResponsePermanentRedirect('/announcements')

    except Announcement.DoesNotExist:
        HttpResponse('Объявление не найдено')