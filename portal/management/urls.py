from django.urls import path, include
from management import views

urlpatterns = [
    path('', include('django.contrib.auth.urls'), name='management'),
]