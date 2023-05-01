from django.http import HttpResponse
from django.shortcuts import render
from .models import Theme

# Логин:lexi-wooo Пароль: 19042002

def without_filter(request):

    # theme1 = Theme.objects.filter(id=1).update(name="Сравнительная характеристика навозных и дождевых червей", author="Коновалов С. М", subject="Природоведение",
    #  status="Свободна", descript="Рыбы любят навозных червей больше, чем дождевых (на последих ничо не клюет)")
    # theme1.save()
    # theme2 = Theme.objects.filter(id=2).update(name="Роль буржуазии в литературе XIX века", author="Еременко Д. Ф", subject="Литература",
    #  status="Свободна", descript="В большинстве случаев мы считаем, что буржуазия была не очень приятным элементом общества, однако если посмотреть подробнее...")
    # theme2.save()
    
    themes = Theme.objects.all()
    return render(request, 'theme_list/theme_list.html', context={"themes": themes})