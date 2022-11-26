from django.http import HttpResponse

def index(request):
    return HttpResponse("""Извините, но вам не доступна эта страница, т.к. у вас нет роли админа, пока что её ни у кого нет, т.к. она не определена в проекте""")
def front(r):
    return HttpResponse(f"""
                        <br><button onclick="location.href='announcements'">Объявления</button> <br> 
                        <button onclick="location.href='management'">Администрирование</button><br>
                        <button onclick="location.href='subjects'">Список тем</button><br>
                        <button onclick="location.href='projects'">Проекты</button><br>""")
