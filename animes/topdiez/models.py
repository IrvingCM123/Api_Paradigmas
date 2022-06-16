from django.db import models

# Create your models here.


class Topdiez(models.Model):
    nombre = models.TextField(blank=True)
    genero = models.TextField(blank=True)
    description = models.TextField(blank=True)
    capitulos = models.TextField(blank=True)
    duracion = models.TextField(blank=True)
    temporadas = models.TextField(blank=True)
    fecha = models.TextField(blank=True)
