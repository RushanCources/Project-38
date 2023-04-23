from django.urls import path, include
from projects import views

urlpatterns = [
    path('', include('django.contrib.auth.urls'), name='project'),
    path('theme_list/', views.theme_list, name='theme_list'),
    path('index/', views.index, name='projects'),
    path('create/', views.send_create_form, name='create'),
    path('create/postcreate/', views.create, name='postcreate'),
    path('correct_project', views.correct_project, name='correct_project'),
    path('create_data', views.create_data),
    path('update_file', views.update_file, name='update_file'),
    path('delete_file', views.delete_file, name='delete_file'),
    path('download_file', views.download_file, name='download_file'),
    path('add_file', views.upload_file, name='add_file'),
    path('trash', views.get_trash, name='trash')
]