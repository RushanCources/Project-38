from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='announcements'),
    path('redactor', views.redactor, name='redactor'),
    path('createannouncement', views.createannouncement, name='createannouncement'),
    path('editor/<int:id>', views.editor, name='editor'),
    path('editor/editannouncement/<int:id>', views.editannouncement, name='editannouncement')
]