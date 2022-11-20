from django.http import HttpResponse

def index(request):
    return HttpResponse("""Здесь долен быть проект и возможность им управлять
                        <br><button onclick="location.href='announcements'">announcements</button> <br> 
                        <button onclick="location.href='management'">management</button><br>
                        <button onclick="location.href='subjects'">subjects</button><br>
                        <button onclick="location.href='projects'">projects</button><br>""")
