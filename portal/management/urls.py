from django.urls import path, include
from .views import register, admin_menu

urlpatterns = [
    path('', include('django.contrib.auth.urls'), name='management'),
    path('register/', register, name = 'register'),
    path('admin_menu/', admin_menu, name='admin_menu')
]