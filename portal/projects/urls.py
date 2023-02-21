from django.urls import path
from projects import views

urlpatterns = [
    path('', views.index, name='projects'),
    path('account/', views.account, name='account'),
    path('create/', views.create, name='create'),
    path('create/postcreate/', views.postcreate, name='postcreate'),
]