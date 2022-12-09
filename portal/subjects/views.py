from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    text = "Здесь должен быть список проетных тем"
    title = "Проектные темы"
    data = {"header" : title, "text" : text}
    return render(request, "index.html", context=data)
