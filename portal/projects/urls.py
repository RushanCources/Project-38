from django.urls import path
from projects import views

urlpatterns = [
    path('', views.index, name='projects'),
    path('create/', views.create, name='create'),
    path('create/postcreate/', views.postcreate, name='postcreate'),
    path('correctProject', views.correctProject, name='correctProject'),
    path('createdata', views.create_data)
]