from django.db import models
# Create your models here.
class Book(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    valoracion = models.IntegerField()

    def __str__(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Valoracion: {self.valoracion}"





