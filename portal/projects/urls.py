from django.urls import path
from projects import views

urlpatterns = [
    path('index/', views.index, name='projects'),  # переводит на страницу пректов, которые есть у юзера или на отдельный проект если указан id
    path('create/', views.send_create_form, name='create'),  # форма для подачи заявки на проект
    path('create/postcreate/', views.create, name='postcreate'),  # обработка формы подачи заявки на проект
    path('correct_project', views.correct_project, name='correct_project'),  # изменение данных проекта
    path('update_file', views.update_file, name='update_file'),  # обновление файла
    path('delete_file', views.delete_file, name='delete_file'),  # перемещение файла в корзину
    path('download_file', views.download_file, name='download_file'),  # загрузка файла на компьютер пользователя
    path('add_file', views.upload_file, name='add_file'),  # добавление фойла в проект
    path('trash', views.get_trash, name='trash'),  # страничка с корзиной
    path('add_comment', views.set_comment, name='add_comment'),  # добавление комментария к файлу
    path('approve_project', views.approve_project, name='approve_project'),  # одобрение заявки на проект
    path('close_project', views.close_project, name='close_project'),  # закрытие работы над проектом
    path("restore_file", views.restore_file, name='restore_file')  # восстановление файла из корзины
]
