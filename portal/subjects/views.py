from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import Theme, Subject
from projects.views import send_create_form
import random


def without_filter(request):
    themes = Theme.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'theme_list/theme_list.html', {'themes': themes, 'subjects': subjects})


def new_theme_create(request):
    if request.method == 'POST':
        theme_id = request.POST.get('theme_id')

        if theme_id == '0':
            theme = Theme.objects.create(
                class_of_tag='tag-open', status='Свободно')
        else:
            theme = Theme.objects.get(id=theme_id)

        theme.name = request.POST.get('name_input')
        theme.descript = request.POST.get('descript_input')
        theme.subjects = request.POST.get('subjects_input')
        theme.author = request.POST.get('author_input')

        theme_subject = request.POST.get('subjects_input')
        theme_subject = theme_subject.split(',')[0]

        if (not Subject.objects.filter(name=theme_subject).exists()):
            color = str(random.randint(45, 255)) + ',' + \
                str(random.randint(45, 255)) + ',' + \
                str(random.randint(45, 255))
            Subject.objects.create(name=theme_subject, color=color)
            theme.subject_color = color
        else:
            subject = Subject.objects.get(name=theme_subject)
            theme.subject_color = subject.color

        theme.save()
    return redirect('theme_list')


def search(request):
    if request.method == 'POST':
        filters_subject = request.POST.get('subject')
        print(filters_subject)
        print(*request.POST.items())
        subjects = Subject.objects.all()
        search_object = request.POST.get('search_input')
        filters_open = request.POST.get('open')
        filters_close = request.POST.get('close')
        filters_past_year = request.POST.get('past_year')
        search_result = Theme.objects.all()
        if filters_open != None:
            search_result = search_result.filter(status='Свободно')
        if filters_close != None:
            search_result = search_result.filter(status='Занято')
        if filters_past_year != None:
            search_result = search_result.filter(status='Прошлых лет')
        if filters_subject != 'Не указано':
            search_result = search_result.filter(
                subjects__icontains=filters_subject)
        search_result = search_result.filter(name__icontains=search_object)
    return render(request, 'theme_list/theme_list.html', {'themes': search_result, 'subjects': subjects})


def use_theme(request: HttpRequest):
    theme_id = request.GET.get('theme_id')
    try:
        theme = Theme.objects.get(id=theme_id)
        context = {'name': theme.name,
                  'description': theme.descript}
        return send_create_form(request, context_data=context)
    except Theme.DoesNotExist:
        redirect('theme_list')
