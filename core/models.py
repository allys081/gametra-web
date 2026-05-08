from django.db import models
from django.contrib.auth.models import User


class Juego(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    # Para saber si lo ve cualquiera
    es_publico = models.BooleanField(default=False)
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Reseña(models.Model):
    juego = models.ForeignKey(
        Juego, on_delete=models.CASCADE, related_name='reseñas')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reseña de {self.usuario.username} en {self.juego.titulo}"
