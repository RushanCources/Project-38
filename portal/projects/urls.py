from django.urls import path, include
from projects import views

urlpatterns = [
    path('', include('django.contrib.auth.urls'), name='project'),
    path('theme_list/', views.theme_list, name='theme_list'),
    path('index/', views.index, name='projects'),
    path('create/', views.send_create_form, name='create'),
    path('create/postcreate/', views.create, name='postcreate'),
    path('correctProject', views.correct_project, name='correctProject'),
    path('create_data', views.create_data),
    path('update_file', views.update_file, name='update_file'),
]