from django.urls import path
from projects import views

urlpatterns = [
    path('', views.index, name='projects'),
]