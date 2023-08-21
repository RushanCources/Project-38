from django.urls import path, include
from subjects import views

urlpatterns = [
    path('', include('django.contrib.auth.urls'), name='subject'),
    path('theme_list/', views.without_filter, name='theme_list'),
    path('theme_create_test/' , views.create_test, name='create_auto'),
    path('new_theme_create/' , views.new_theme_create, name='new_theme_create'),
    path('search_results_view', views.search, name='search_results_view'),
]
