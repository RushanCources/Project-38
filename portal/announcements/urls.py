from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('/redactor', views.redactor),
    path('/redactor/<int:id>', views.redactor),
    path('/createannouncement', views.createannouncement)
]