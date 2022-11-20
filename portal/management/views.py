from django.http import HttpResponse

def index(request):
    return HttpResponse("""Здесь должна быть авторизация админа и последующее администрирование
                        <br><button onclick="location.href='announcements'">announcements</button> <br> 
                        <button onclick="location.href='management'">management</button><br>
                        <button onclick="location.href='subjects'">subjects</button><br>
                        <button onclick="location.href='projects'">projects</button><br>""")
def front(r):
    return HttpResponse(f"""
                        <br><button onclick="location.href='announcements'">announcements</button> <br> 
                        <button onclick="location.href='management'">management</button><br>
                        <button onclick="location.href='subjects'">subjects</button><br>
                        <button onclick="location.href='projects'">projects</button><br>""")
