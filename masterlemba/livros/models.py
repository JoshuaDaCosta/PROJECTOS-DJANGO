from django.db import models


class Livros(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    data_pub = models.DateField()

    def __str__(self):
        return self.titulo
