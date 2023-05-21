from django.urls import path, include
from subjects import views

urlpatterns = [
    path('', include('django.contrib.auth.urls'), name='subject'),
    path('theme_list/', views.without_filter, name='theme_list'),
    path('theme_create/' , views.create_auto, name='create_auto'),
]