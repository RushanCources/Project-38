from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse, HttpResponsePermanentRedirect
from .models import Announcement
from datetime import date
from .decorators import allowed_users
from .models import File
from .forms import AnnouncementForm


# Добавить проверку форм при удалении тестовых шаблонов


def index(request):

    group = None
    superuser = False
    announcements = Announcement.objects.all()

    if request.user.groups.exists():
        group = request.user.groups.all()[0].name
    if group in ['Teacher', 'admin']:
        superuser = True

    data = {'superuser': superuser,
            'announcements': announcements}

    return render(request, 'dec/dec.html', context=data)


#@allowed_users(allowed_roles=['Teacher', 'admin'])
def redactor(request):
    form = AnnouncementForm()
    return render(request, "announcements/redactor.html", context={'form': form})


#@allowed_users(allowed_roles=['Teacher', 'admin'])
def createannouncement(request):

    if request.method != "POST":
        return HttpResponsePermanentRedirect("/announcements")

    title = request.POST.get("title")
    body = request.POST.get("body")
    is_pinned = request.POST.get("is_pinned")
    de = request.POST.get("date_of_expiring")
    author = request.user
    files = request.FILES.getlist('files')
    image_url = request.POST.get("image_url")

    de = de.split("-")

    announcement = Announcement.objects.create(title=str(title), body=str(body), is_pinned=bool(is_pinned), date_of_expiring=date(int(de[0]), int(de[1]), int(de[2])), author=author, image_url=image_url)

    for file in files:
        File.objects.create(announcement=announcement, file=file)

    return HttpResponsePermanentRedirect('/announcements')


#@allowed_users(allowed_roles=['Teacher', 'admin'])
def editor(request, id):
    try:
        announcement = Announcement.objects.get(id=id)
        initial_data = {
            'title': announcement.title,
            'body': announcement.body,
            'is_pinned': announcement.is_pinned,
            'date_of_expiring': str(Announcement.objects.get(id=id).date_of_expiring)[:10],
            'image_url': announcement.image_url,
        }

        form = AnnouncementForm(initial=initial_data)

        data = {
            'form': form,
            'announcement_id': id,
            'announcement': announcement,
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
        is_pinned = request.POST.get("is_pinned", False)
        if is_pinned : is_pinned = True
        files_to_add = request.FILES.getlist('files')
        files_to_delete = request.POST.getlist('file_id_to_delete[]')
        image_url = request.POST.get('image_url')

        for file_id in files_to_delete:
            file = File.objects.get(pk=int(file_id))
            file.file.delete()
            file.delete()

        for file in files_to_add:
            File.objects.create(announcement=announcement, file=file)

        announcement.title = request.POST.get("title")
        announcement.body = request.POST.get("body")
        announcement.is_pinned = is_pinned
        announcement.date_of_expiring = date_of_expiring
        announcement.image_url = image_url

        announcement.save()

        return HttpResponsePermanentRedirect('/announcements')

    except Announcement.DoesNotExist:
        HttpResponse('Объявление не найдено')


def search(request):
    query = request.GET.get('q')
    if query:
        announcements = Announcement.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
    else:
        announcements = Announcement.objects.all()
    context = {
        'announcements': announcements,
        'search_value': query,
    }
    return render(request, 'dec/dec.html', context=context)
