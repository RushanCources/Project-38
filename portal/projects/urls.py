from django.urls import path, include
from projects import views

urlpatterns = [
    path('', include('django.contrib.auth.urls'), name='project'),
    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('create/postcreate/', views.postcreate, name='postcreate'),
    path('correctProject', views.correctProject, name='correctProject'),
    path('createdata', views.create_data)
]