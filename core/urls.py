from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('perfil/', views.perfil, name='perfil'),
    path('juegos/', views.juegos, name='juegos'),
    path('juego/<int:juego_id>/', views.detalle_juego,
         name='detalle_juego'),  # ESTA FALTABA
    path('nuevo-juego/', views.crear_juego,
         name='crear_juego'),               # ESTA FALTABA
    path('resena/<int:juego_id>/', views.dejar_resena,
         name='dejar_resena'),   # ESTA FALTABA
    path('registro/', views.registro, name='registro'),
    # Agrega estas dos líneas junto a las otras rutas
    path('juego/<int:juego_id>/eliminar/',
         views.eliminar_juego, name='eliminar_juego'),
    path('resena/<int:resena_id>/eliminar/',
         views.eliminar_resena, name='eliminar_resena'),
]
