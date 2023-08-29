from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse, HttpResponsePermanentRedirect
from .models import Announcement
from datetime import date
from .decorators import allowed_users
from .models import File
from .forms import AnnouncementForm
from django.core.paginator import Paginator
from django.conf import settings
from pathlib import Path
import os


# ToDo: Добавить проверку форм при удалении тестовых шаблонов


def index(request):

    group = None
    superuser = False
    anns = Announcement.objects.all()

    paginator = Paginator(anns, 20) # Batch size здесь (см dec.html)
    page_number = request.GET.get('page')
    page_announcements = paginator.get_page(page_number)

    if request.user.groups.exists():
        group = request.user.groups.all()[0].name
    if group in ['Teacher', 'admin']:
        superuser = True

    data = {'superuser': superuser, 'page_announcements': page_announcements}

    return render(request, 'dec/dec.html', context=data)


#@allowed_users(allowed_roles=['Teacher', 'admin'])
def redactor(request):
    """Отвечает за рендер шаблона редактора со всеми формами"""

    covers_dir = settings.BASE_DIR / "media" / "covers"
    covers = []

    for cover in os.listdir(covers_dir):
        covers.append("/media/covers/" + cover)

    form = AnnouncementForm()
    return render(request, "dec/red.html", context={'form': form, 'covers': covers})


#@allowed_users(allowed_roles=['Teacher', 'admin'])
def createannouncement(request):
    """Создает объявление (Записывает в БД)"""

    if request.method != "POST":
        return HttpResponsePermanentRedirect("/announcements")

    form = AnnouncementForm(request.POST)

    if form.is_valid():
        pass
    else:
        return render(request, 'WrongData.html')

    title = request.POST.get("title")
    body = request.POST.get("body")
    is_pinned = request.POST.get("is_pinned")
    de = request.POST.get("date_of_expiring")
    author = request.user
    files = request.FILES.getlist('files')
    image_url = request.POST.get("image_url")

    announcement = Announcement.objects.create(title=str(title), body=str(body), is_pinned=bool(is_pinned), author=author, image_url=image_url)

    if de:
        de = de.split("-")
        announcement.date_of_expiring = date(int(de[0]), int(de[1]), int(de[2]))
        announcement.save()

    for file in files:
        File.objects.create(announcement=announcement, file=file)

    return HttpResponsePermanentRedirect('/announcements')


#@allowed_users(allowed_roles=['Teacher', 'admin'])
def editor(request, id):
    """Отвечает за рендер шаблона эдитора объявлений со всеми формами и прошлыми данными"""

    try:
        announcement = Announcement.objects.get(id=id)
        initial_data = {
            'title': announcement.title,
            'body': announcement.body,
            'is_pinned': announcement.is_pinned,
            'date_of_expiring': str(Announcement.objects.get(id=id).date_of_expiring)[:10],
            'image_url': announcement.image_url,
        }

        covers_dir = settings.BASE_DIR / "media" / "covers"
        covers = []

        for cover in os.listdir(covers_dir):
            covers.append("/media/covers/" + cover)

        form = AnnouncementForm(initial=initial_data)

        data = {
            'form': form,
            'announcement_id': id,
            'announcement': announcement,
            'covers': covers
        }

        return render(request, 'dec/ed.html', context=data)

    except Announcement.DoesNotExist:
        return render(request, 'WrongData.html')


#@allowed_users(allowed_roles=['Teacher', 'admin'])
def editannouncement(request, id):
    """Отвечает за редактирование объявления (изменение существующих значений в БД)"""

    try:

        if request.method != "POST":
            return HttpResponsePermanentRedirect('/announcements')

        announcement = Announcement.objects.get(id=id)
        de = request.POST.get("date_of_expiring").split("-")
        if de != ['']:
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
        if de != ['']:
            announcement.date_of_expiring = date_of_expiring
        else:
            announcement.date_of_expiring = None
        announcement.image_url = image_url

        announcement.save()

        return HttpResponsePermanentRedirect('/announcements')

    except Announcement.DoesNotExist:
        return render(request, 'WrongData.html')


def search(request):
    """Отвечает за функциональную часть поиска"""

    query = request.GET.get('q')
    query_words = query.split()
    query_filter = Q()

    for word in query_words:
        query_filter |= Q(title__icontains=word) | Q(body__icontains=word) | Q(
            author__first_name__icontains=word) | Q(author__last_name__icontains=word)

    anns = Announcement.objects.filter(query_filter)

    paginator = Paginator(anns, 20)
    page_number = request.GET.get('page')
    page_announcements = paginator.get_page(page_number)

    data = {
        'page_announcements': page_announcements,
        'search_value': query,
    }
    return render(request, 'dec/dec.html', context=data)


def announcement(request, id):
    try:
        announcement = Announcement.objects.get(id=id)

    except Announcement.DoesNotExist:
        return render(request, 'WrongData.html')

    context = {
        'announcement': announcement,
    }

    return render(request, 'dec/ann.html', context=context)


#@allowed_users(allowed_roles=['Teacher', 'admin'])
def delete_announcement(request, id):
    """Удаляет просроченные объявления и связанные с ними файлы"""

    if request.method != 'GET':
        return render(request, 'WrongData.html')

    announcement = Announcement.objects.get(id=id)

    files = announcement.files.all()

    for file in files:
        file.file.delete()
        file.delete()

    announcement.delete()

    return HttpResponsePermanentRedirect('/announcements')
