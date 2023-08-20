from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Theme


def without_filter(request):
    themes = Theme.objects.all()
    return render(request, 'theme_list/theme_list.html' , {'themes': themes})

def create_auto(request):
    theme = Theme.objects.create(Name = "123", Author = "123", Subject = "123", Status = "Свободно", Descript = "Тут что-то", Class_of_subject = "theme-block theme-block-close sub2", Class_of_tag = "teg teg-open")
    return redirect('theme_list')

def new_theme_create(request):
    if request.methood == 'POST':
        theme = Theme()
        theme.name = request.POST.get('name_input')
        theme.descript = request.POST.get('descript_input')
        theme.subjects = request.POST.get('subjects_input')
        theme.author = request.POST.get('author_input')
        theme.save()
    return redirect('theme_list')