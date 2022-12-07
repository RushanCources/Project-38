from django.urls import path
from navigation import views
 
urlpatterns = [
    path('', views.index, name='home'),
]
