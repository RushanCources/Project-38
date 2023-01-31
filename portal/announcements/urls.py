from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('/redactor', views.redactor),
    path('/createannouncement', views.createannouncement)
]