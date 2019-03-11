from django.db import models
from pacientes.models import Paciente

# Create your models here.


class Prescricao(models.Model):
    prescricao = models.TextField()
    anotacoes = models.TextField()
    data = models.DateField()
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='prescricoes', null=True, blank=True)

    def __str__(self):
        return self.paciente.nome + ' ' + self.prescricao + ' ' + self.anotacoes
