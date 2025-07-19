from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('wallpaper/', views.wallpaper, name='wallpaper'),
    path('audio/', views.audio, name='audio'),
]
