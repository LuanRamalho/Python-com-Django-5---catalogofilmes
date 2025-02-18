from django.db import models

class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    diretor = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    ano = models.IntegerField()
    sinopse = models.TextField()
    capa = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.titulo
