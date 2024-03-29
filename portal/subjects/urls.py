from django.urls import path, include
from subjects import views

urlpatterns = [
    path('theme_list/', views.without_filter, name='theme_list'),
    path('new_theme_create/', views.new_theme_create, name='new_theme_create'),
    path('search_results_view', views.search, name='search_results_view'),
    path(route='use_theme', view=views.use_theme, name='use_theme'),
]
