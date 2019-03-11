from django.db import models

# Create your models here.


class Paciente(models.Model):
    nome = models.CharField(max_length=150)
    leito = models.IntegerField()
    prontuario = models.IntegerField()

    def __str__(self):
        return self.nome