from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Theme, Subject
import random


def without_filter(request):
    themes = Theme.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'theme_list/theme_list.html' , {'themes': themes, 'subjects' : subjects})

def create_test(request):
    theme = Theme.objects.create(Name = "123", Author = "123", Subject = "123", Status = "Свободно", Descript = "Тут что-то", Class_of_subject = "sub2", Class_of_tag = "tag-open")
    return redirect('theme_list')

def new_theme_create(request):
    if request.method == 'POST':
        theme_id = request.POST.get('theme_id')

        if theme_id == 0:
            theme = Theme.objects.create(class_of_tag ='tag-open', status='Свободно')
        else:
            theme = Theme.objects.get(id=theme_id)

        theme.name = request.POST.get('name_input')
        theme.descript = request.POST.get('descript_input')
        theme.subjects = request.POST.get('subjects_input')
        theme.author = request.POST.get('author_input')

        theme_subject = request.POST.get('subjects_input')
        theme_subject = theme_subject.split(',')[0]
    
        if (not Subject.objects.filter(name=theme_subject).exists()):
            color = str(random.randint(45,255)) + ',' + str(random.randint(45,255)) + ',' + str(random.randint(45,255))
            Subject.objects.create(name=theme_subject,color=color)
            theme.subject_color = color
        else:
            subject = Subject.objects.get(name=theme_subject)
            theme.subject_color = subject.color  
            
        theme.save()

    return redirect('theme_list')