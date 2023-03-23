from django.urls import path, include
from projects import views

urlpatterns = [
    path('', include('django.contrib.auth.urls'), name='project'),
    path('theme_list/', views.theme_list, name='theme_list'),
    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('create/postcreate/', views.postcreate, name='postcreate'),
    path('serchscript', views.jslibs, name='select2'),
    path('jquery', views.jslibs, name='jquery'),
    path('select2css', views.csslibs, name='selec2css')
]