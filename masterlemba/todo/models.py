from django.db import models
from datetime import date 
from django.contrib.auth.models import User 

# Create your models here.


class Todo(models.Model):
    usuario=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    titulo = models.CharField(verbose_name="Título", max_length=100, null=False, blank=False)
    criado_em = models.DateField(auto_now_add=True, null=False, blank=False)
    data_entrega = models.DateField(verbose_name="Data de entrega", null=False, blank=False)
    finalizado_em = models.DateField(null=True)

    class meta:
        ordering=["data_entrega", "criado_em"]
    def marcar_completo(self):
        if not self.finalizado_em:
            self.finalizado_em=date.today()
            self.save()
    def __str__(self):
        return self.titulo
