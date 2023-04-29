from django.http import HttpResponse
from django.shortcuts import render


def without_filter(request):
    return render(request, 'theme_list/theme_list.html')