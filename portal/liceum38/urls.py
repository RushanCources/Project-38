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
from django.views.generic import TemplateView
from announcements import views as v1
from management import views as v2
from subjects import views as v3
from projects import views as v4

urlpatterns = [
    path('announcements', v1.index, name='announcements'),
    path('management/', include('management.urls')),
    path('subjects', v3.index, name='subjects'),
    path('projects/', include('projects.urls')),
    path('', TemplateView.as_view(template_name = 'home.html'), name='home'),
    #path('admin/', admin.site.urls),
]
