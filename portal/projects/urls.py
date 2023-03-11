from django.urls import path, include
from projects import views

urlpatterns = [
    path('', include('django.contrib.auth.urls'), name='project'),
    path('theme_list/', views.theme_list, name='theme_list'),
]