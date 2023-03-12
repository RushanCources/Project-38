from django.shortcuts import render

def theme_list(request):
    return render(request, 'theme_list/theme_list.html') 

