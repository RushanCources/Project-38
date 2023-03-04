from django.urls import path
from projects import views

urlpatterns = [
    path('', views.index, name='projects'),
    path('create/', views.create, name='create'),
    path('create/postcreate/', views.postcreate, name='postcreate'),
    path('serchscript', views.jslibs, name='select2'),
    path('jquery', views.jslibs, name='jquery'),
    path('select2css', views.csslibs, name='selec2css')
]