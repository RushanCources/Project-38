from django.http import HttpResponse

def index(request):
    return HttpResponse("""Здесь долен быть проект и возможность им управлять
                        <br><button onclick="location.href='announcements'">Объявления</button> <br> 
                        <button onclick="location.href='management'">Администрирование</button><br>
                        <button onclick="location.href='subjects'">Список тем</button><br>
                        <button onclick="location.href='projects'">Проекты</button><br>""")
