from django.db import models


class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
