from django.urls import path, include
from .views import register, admin_menu, token_page, profile

urlpatterns = [
    path('', include('django.contrib.auth.urls'), name='management'),
    path('register/', register, name = 'register'),
    path('token_page/', token_page, name = 'token_page'),
    path('admin_menu/', admin_menu, name='admin_menu'),
    path('profile/', profile, name='profile'),
]