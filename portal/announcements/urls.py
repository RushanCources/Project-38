from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='announcements'),
    path('redactor', views.redactor, name='redactor'),
    path('createannouncement', views.createannouncement, name='createannouncement')
]