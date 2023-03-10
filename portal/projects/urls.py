from django.urls import path
from projects import views

urlpatterns = [
    path('', views.index, name='projects'),
    path('create/', views.create, name='create'),
    path('create/postcreate/', views.postcreate, name='postcreate'),
    path('select2', views.jslibs, name='select2'),
    path('jquery', views.jslibs, name='jquery'),
    path('select2css', views.csslibs, name='select2css'),
    path('correctProject', views.correctProject, name='correctProject')
]