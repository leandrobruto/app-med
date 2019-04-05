from django.db import models

# Create your models here.


class Paciente(models.Model):
    nome = models.CharField(max_length=150)
    prontuario = models.IntegerField(null=True, blank=True)
    leito = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nome