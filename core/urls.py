from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('perfil/', views.perfil, name='perfil'),
    path('juegos/', views.juegos, name='juegos'),
    path('registro/', views.registro, name='registro'),
]
