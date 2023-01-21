"""liceum38 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from management import views as v2
from subjects import views as v3
from projects import views as v4

urlpatterns = [
    path('announcements', include('announcements.urls')),
    path('management', v2.index),
    path('subjects', v3.index),
    path('projects', v4.index),
    path('', v2.front),
    #path('admin/', admin.site.urls),
]
