from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='announcements'),
    path('redactor', views.redactor, name='redactor'),
    path('createannouncement', views.createannouncement, name='createannouncement'),
    path('redactor/<int:id>', views.editor, name='editor'),
    path('redactor/editannouncement/<int:id>', views.editannouncement, name='editannouncement'),
    path('search/', views.search, name='search'),
    path('<int:id>', views.announcement, name='announcement'),
    path('delete/<int:id>', views.delete_announcement, name='delete'),
    path('upload_image/', views.upload_image, name='upload_image'),
]