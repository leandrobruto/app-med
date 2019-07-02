from django.db import models
from medicamentos.models import Medicamento

# Create your models here.


class Aprazamento(models.Model):
    medicamento = models.ForeignKey(Medicamento, related_name='aprazamentos', on_delete=models.CASCADE)
    erro = models.CharField(max_length=20, null=True, blank=True)
    data_programada = models.DateField()
    hora_programada = models.TimeField()
    data_aplicacao = models.DateField(null=True, blank=True)
    hora_aplicacao = models.TimeField(null=True, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
            return str(self.data_programada)
